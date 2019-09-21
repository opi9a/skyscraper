
import os
from os import get_terminal_size
import sys
from collections import OrderedDict
import pickle
import argparse
import getpass

import subprocess
import requests
from bs4 import BeautifulSoup
import re

import pandas as pd

from termcolor import cprint, colored

from mylogger import get_timelog

USER = getpass.getuser()
BASE_PATH = '/home/' + USER + '/shared/projects/skyscraper/'

# strings to trim off if at start of title (with variants)
TRIM_STRINGS = [
    'nfl',
    'nba',
    'cycling',
    'live',
]


def games_by_game(games):
    """
    For an input list of a day's worth of games, group by title
    """

    day_games = OrderedDict()
    print('in it')
    return sorted(games, key=lambda x: x['title'])


def print_games(tidied, days=1, by_title=True):
    """
    Show games on command line.
    """
    log.info("new call to print games")

    term_cols = get_terminal_size()[0]

    pad2, pad3 = 28, 12

    pad1 = term_cols - pad2 - (pad3 * 2) - 3

    for i, day in enumerate(tidied):
        if i == days:
            break

        print("")
        cprint(" " + tidied[day]['day'], attrs=['bold'])
        print("")

        # avoid duplicates (may be different channels)
        games_printed = set()

        games_to_print = tidied[day]['games']

        if by_title:
            games_to_print = sorted(games_to_print, key=lambda x: x['title'])

        last_title = None

        for game in games_to_print:

            out_str = "".join([
                game['title'][:pad1].ljust(pad1),
                game['channel'].split()[0][:pad2].rjust(pad2),
                game['type'][:pad3].rjust(pad3),
                game['time'][:pad3].rjust(pad3)
            ])

            if last_title is not None and game['title'] != last_title:
                out_str = "\n "+ out_str 

            if out_str not in games_printed:
                print(" " + out_str)
                games_printed.add(out_str)

            if by_title:
                last_title = game['title']

    log.info("finished printing games")


def is_game(title):
    """
    Boolean test for whether a title is a game, and does not
    contain one of a list of excluded flags.
    """

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
    """
    Tidies up a title, trimming a number of common undesirable elements.
    """

    REs = [
        # trim 'nba' or 'nfl', with or without 'live' prepend
        re.compile(r'^(live)?[ :]*((nfl)|(nba))?[ :-]*',
                   re.IGNORECASE),

        # trim variants of 'hlts'
        re.compile(r'\s?\bhlts?\b[ :]*', re.IGNORECASE),

        # trim prepended 'cycling' and variants
        re.compile(r'^cycling[ :-]*(?=\w)',
                   re.IGNORECASE),
    ]

    for r in REs:
        title = re.sub(r, "", title)

    return title


def get_cached(type, number_days, dir_path=BASE_PATH):
    """
    Return cached raw list of shows if it exists.
    Type from ['sky', 'eurosport']
    """

    cached_dir_path = os.path.join(dir_path, 'cached_raw', type)
    now = pd.datetime.now()
    today_string = now.strftime("%d-%m-%Y")

    # get files with today_string
    today_files = [f for f in os.listdir(cached_dir_path)
                     if f.startswith(today_string)]

    # stop if no files for today
    if not today_files:
        return False

    # stop if files for today but not long enough
    max_days_hence = max([int(x.split('_')[1].split('d')[0])
                  for x in today_files])

    if max_days_hence < number_days:
        return False

    file_to_load = os.path.join(cached_dir_path,
                              f'{today_string}_{max_days_hence}d.pkl')

    with open(file_to_load, 'rb') as fp:
        cached = pickle.load(fp)

    return cached


def get_raw_sky_shows(number_days, _debug=False, use_cached=True,
                      dir_path=BASE_PATH):
    """
    Main function for retrieving sky shows.

    Returns a raw list of shows, each a dict with fields:
        - title
        - channel
        - datetime (pandas timestamp format)
        - duration (int, minutes)
        - show_type (if found: replay, live etc)

    Works by calling get_sky_games_day() for each in a series of
    days into the future - each of which has a separate web page.
    """

    log.info('getting sky shows')
    now = pd.datetime.now()
    today_string = now.strftime("%d-%m-%Y")

    # see if it exists already
    if use_cached:
        log.info('looking for cached sky games')
        cached = get_cached('sky', number_days, dir_path=dir_path)
        if cached:
            log.info(f'found {len(cached)} cached shows')
            return cached

    url_base = "http://www.skysports.com/watch/tv-guide/"

    now = pd.datetime.now()
    list_out = []
    channels_table = None

    for i in range(number_days):

        # do the scraping for the day
        day_string = now.strftime("%d-%m-%Y")
        url = url_base + day_string 

        log.info('getting sky shows for ' + day_string)
        log.info('url: ' + url)
        req = requests.get(url)

        if not req.ok:
            print('FAILED to get', url)
            continue

        soup = BeautifulSoup(req.text, "html.parser")

        # check if channels table has been populated yet or nah
        if channels_table is None:
            channels_table = get_sky_channels_table(soup)

        # actually get the list of parsed games for this day
        day_games = get_sky_games_day(soup, channels_table, now)
        log.info(f'found {len(day_games)} games')

        # add to the list of games
        list_out.extend(day_games)

        now += pd.Timedelta('1 days')

    # save out
    path_out = os.path.join(dir_path, 'cached_raw', 'sky',
                            f'{today_string}_{number_days}d.pkl')

    log.info(" ".join(['found', str(len(path_out)), 'raw records']))
    log.info(" ".join(['saving to', path_out]))

    with open(path_out, 'wb') as fp:
        pickle.dump(list_out, fp)

    return list_out


def get_sky_channels_table(soup):
    """
    Return a list of ID numbers for channels.
    These numbers appear in the listings for each program, giving a 
    way of assigning channels to shows.
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
    Parses the sky soup for a day and returns
    a list of qualifying shows (['nba', 'nfl']) for that day.
    
    Called by get_raw_sky_shows which does the scraping and makes the soup. 
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


def get_raw_eurosport_shows(number_days=7, use_cached=True, raw_text=None,
                            dir_path=BASE_PATH):
    """
    Scrapes all shows from eurosport schedule and returns list of dicts
    of cycling shows, with following fields:
        - title
        - channel (Eurosport 1 or 2)
        - datetime (pandas timestamp format)
        - duration (int, minutes)
        - show_type (if found: replay, live etc)

    Pass html to raw_text to avoid scraping (debug only)
    """
    log.info('getting eurosport shows')
    
    # see if it exists already
    if use_cached:
        log.info('looking for cached eurosport games')
        cached = get_cached('eurosport', number_days, dir_path=dir_path)
        if cached:
            log.info(f'found {len(cached)} cached shows')
            return cached

    target = re.compile(r"[C|c]ycling")   

    if raw_text is None:

        url = "https://www.eurosport.co.uk/eurosport-tv-schedule.shtml"

        # REQUESTS STOPPED WORKING for this url 12/9/2019, so using curl
        # req = requests.get(url)

        # if not req.ok:
        #     print('could not get', url, 'exiting')
        #     return 1

        # raw_text = req.text

        raw_text = subprocess.run(['curl', url], stdout=subprocess.PIPE).stdout

    soup = BeautifulSoup(raw_text, "html.parser")

    # need an initial cut to get rid of games on now (duplicated below)
    soup = soup.find('div', {'class': 'all-schedule'})

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

    # save out
    now = pd.datetime.now()
    today_string = now.strftime("%d-%m-%Y")
    path_out = os.path.join(dir_path, 'cached_raw', 'eurosport',
                            f'{today_string}_{number_days}d.pkl')

    log.info('saving to ' + path_out)

    with open(path_out, 'wb') as fp:
        pickle.dump(shows_out, fp)

    log.info('length shows_out ' + str(len(shows_out)))
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

    i = 0
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


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='print coming sky shows')
    parser.add_argument('days_hence', nargs='?', default=1, type=int)
    parser.add_argument('-p', '--dir-path', default=BASE_PATH)

    args = parser.parse_args()

    print(args)

    # set up a logger
    log = get_timelog(os.path.join(args.dir_path, 'logs/skyscraper.log.txt'))
    
    log.info("="*50)
    log.info(f"main script called for {args.days_hence} days")

    # these raw outputs are lists of shows
    # each show a dict with sensible keys ('title', 'datetime' etc)
    # mainly overlapping between sky and eurosport
    cycling_raw = get_raw_eurosport_shows(dir_path=args.dir_path)
    sky_raw = get_raw_sky_shows(args.days_hence, dir_path=args.dir_path)

    # make them into a structure based on days
    tidied = tidy_shows(sky_raw + cycling_raw)

    print_games(tidied, args.days_hence)
    print("")
