from bs4 import BeautifulSoup
import re
import requests
from datetime import datetime as dt
from datetime import timedelta
from collections import OrderedDict
import calendar
from pprint import pprint
from operator import itemgetter
import pandas as pd

# strings to trim off if at start of title (with variants)
TRIM_STRINGS = [
    'nfl',
    'nba',
    'cycling',
    'live',
]

def is_game(title):

    # drop non games
    drop_flags = [
        'gametime',
        'nba action',
        'inside the nba',
        'great games',
        'a football life',
    ]

    is_game = True

    for flag in drop_flags:
        if flag in title.lower():
            is_game = False

    return is_game


def clean_title(title):

    REs = [
        re.compile(r'^(live)?[ :]*((nfl)|(nba))?[ :-]*',
                   re.IGNORECASE),

        re.compile(r'\s?\bhlts?\b[ :]*', re.IGNORECASE),

        re.compile(r'^cycling[ :-]*(?=\w)',
                   re.IGNORECASE),
    ]

    for r in REs:
        title = re.sub(r, "", title)

    return title


def get_shows(number_days, _debug=False):

    url_base = "http://www.skysports.com/watch/tv-guide/"

    now = pd.datetime.now()
    list_out = []
    channels_table = None

    for i in range(number_days):

        day_string = now.strftime("%d-%m-%Y")
        url = url_base + day_string 

        print('getting', url)
        req = requests.get(url)

        if not req.ok:
            print('FAILED')
            continue

        soup = BeautifulSoup(req.text, "html.parser")

        if channels_table is None:
            channels_table = get_sky_channels_table(soup)

        list_out.extend(get_sky_games_day(soup, channels_table, now))

        now += pd.Timedelta('1 days')

    return list_out



def get_sky_channels_table(soup):
    """
    Return a list of ID numbers for channels.
    These numbers appear in the listings for each program, giving a 
    different (better) way of assigning channel.

    Not yet implemented
    """

    id_re = re.compile(r"channels/([\d]+)")

    channels_table = OrderedDict()

    channels_html = soup.find_all("span", {"class": "ss-tvlogo"})

    for channel in channels_html:
        tag = channel.find('img')
        id = id_re.findall(tag.get('src'))[0]
        channels_table[id] = tag.get('alt').strip()

    return channels_table


def get_sky_games_day(soup, channels_table, date):
    """
    Called by get_shows.  Processes the soup.
    """

    SKY_RE = re.compile(r'\bnba\b|\bnfl\b', re.IGNORECASE)
    CHAN_RE = re.compile(r'prog/(\d+)/')

    games = []

    for game in soup.find_all("h4", text=SKY_RE): 
        game_dict = {}
        game_dict['link'] = game.parent.get('href')
        game_dict['title'] = game.text.strip()

        channel_id = CHAN_RE.findall(game_dict['link'])[0]
        game_dict['channel'] = channels_table.get(channel_id, None)

        game_dict['title'] = game.text.strip()

        time_dur = game.parent.find('p',
                               {"class": "-time"}).text.strip().split(",")

        game_dict['duration'] = int(time_dur[1].strip().split()[0])

        time_obj = pd.datetime.strptime(time_dur[0].upper(), "%I:%M%p")

        date_time_obj = pd.datetime(hour=time_obj.hour,
                                            minute=time_obj.minute,
                                            day=date.day,
                                            month=date.month,
                                            year=date.year)
        game_dict['datetime'] = pd.to_datetime(date_time_obj) 

        for sport in ['nba', 'nfl']:
            if sport in game_dict['title'].lower():
                game_dict['sport'] = sport

        games.append(game_dict)

    return games


def get_eurosport_cycling():
    """
    Scrapes all shows from eurosport schedule and returns dict of cycling 
    shows, with following fields:
        - title
        - channel (Eurosport 1 or 2)
        - datetime (pandas timestamp format)
        - duration (int, minutes)
        - show_type (if found: replay, live etc)
    """
    
    target = re.compile(r"[C|c]ycling")   

    url = "https://www.eurosport.co.uk/eurosport-tv-schedule.shtml"
    req = requests.get(url)

    if not req.ok:
        print('could not get', url, 'exiting')
        return 1

    soup = BeautifulSoup(req.text, "html.parser")

    bottom_level = soup.find_all("div",
                                 {"class": "tv-program__event"},
                                 text=target)

    raw_shows = [s.parent.parent for s in bottom_level]
    shows_out = []


    for i, raw_show in enumerate(raw_shows):
        show_dict = {}

        show_dict['title'] = raw_show.find(
                            "div", {"class": "tv-program__event"}).text

        show_dict['channel'] = 'Eurosport ' + raw_show.get('data-ch-id')[-1]

        show_dict['datetime'] = pd.to_datetime(raw_show.get('data-startdate'))
        show_dict['duration'] = int(raw_show.get('data-totalminutes')) 

        try:
            show_dict['show_type'] = raw_show.find('div',
                                       {'class': 'tv-program__label'}).text
        except:
            show_dict['show_type'] = 'not_found'

        show_dict['sport'] = 'cycling'

        shows_out.append(show_dict)


    return shows_out


def tidy_shows(shows_list, games_only=True):
    """
    Take a list of dicts with structure:
        - title
        - channel (Eurosport 1 or 2)
        - datetime (pandas timestamp format)
        - duration (int, minutes)
        - show_type (if found: replay, live etc)

    And make an OrderedDict of dates ('12-03-2019', '13-03-2019', ..),
    each date being a dict with fields:
        - day (eg 'Monday', 'Tuesday')
        - games, a list of dicts each with fields:
            - game (the title, eg 'NFL Live: Buffalo @ Miami')
            - time (eg '8:00 pm')
            - u_time (in minutes, so utc // 60 (?) - think redundant)
            - type ('nba', 'nfl', 'cycling')
    """

    shows_by_day = OrderedDict()

    link_url_base = "https://www.skysports.com/"

    cutoff_time = pd.datetime.now() - pd.Timedelta('3 hours')

    for show in sorted(shows_list, key=lambda x: x['datetime']):

        # winnow out non-games
        if games_only and not is_game(show['title']):
            continue

        if show['datetime'] < cutoff_time:
            continue

        # make the tidied entry for the show
        game = {}
        game['title'] = clean_title(show['title'])
        game['time'] = show['datetime'].strftime("%-I:%M %P")
        game['u_time'] = int(show['datetime'].value // (60 * 10**9))
        game['sport'] = show['sport']
        game['channel'] = show['channel']

        game['type'] = infer_type(show)

        if 'link' in show.keys():
            game['link'] = link_url_base + show['link']
        else:
            game['link'] = 'X' # need this for jinja to evaluate it

        if show['datetime'].hour < 4:
            datetime = (show['datetime'] - pd.Timedelta('1 days'))
        else:
            datetime = show['datetime']

        date = datetime.strftime("%d-%m-%Y")

        # if it is the first show on the date, make a dict entry for the date
        if date not in shows_by_day:
            shows_by_day[date] = {'day': datetime.strftime("%A"),
                                  'games': []}

        shows_by_day[date]['games'].append(game)


    return shows_by_day


def infer_type(game):
    """
    Tries to work out what type of show, from:
        ['Live', 'Highlights', 'Replay', 'Historical',
         'Other', 'Unknown', 'Magazine', 'Insania']
    """

    if 'show_type' in game.keys():
        return game['show_type'].title()

    title = game['title'].lower()

    if 'live' in title:
        return 'Live'

    if 'gametime' in title:
        return 'Magazine'

    if 'great games' in title:
        return 'Historical'

    if 'nba action' in title:
        return 'Magazine'

    if 'hlts' in title:
        return 'Highlights'

    if 'redzone' in title:
        return 'Insania'

    return 'Unknown'


def join_tidied(sky_tidy, cycling_tidy):
    """
    Join tidied ordered dicts.
    Just extend the games list for each day, taking sky as the start point.
    """

    if not cycling_tidy:
        return sky_tidy

    for day in sky_tidy:
        sky_tidy[day]['games'].extend(cycling_tidy[day]['games'])
    
    return sky_tidy


def get_by_game(tidied):
    '''Takes a dict organised by date, and returns on organised by game (then date)
    '''
    by_game = {}

    # make the dict
    for day in tidied:
        for show in tidied[day]['games']:
            # print("show is ", show)
            show['day']=tidied[day]['day']
            show['date']=day
            
            # can do this better with dict.setdefault() I think
            if show['title'] not in by_game:
                by_game[show['title']]=[show]
            else: 
                by_game[show['title']].append(show)


    # take out redzone  
    by_game.pop('Redzone', None)

    return by_game
