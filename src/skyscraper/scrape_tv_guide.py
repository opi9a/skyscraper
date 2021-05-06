# skyscraper/scrape_tv_guide.py
"""
Scripts to get shows from www.tvguide.co.uk
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import pandas as pd

from .constants import DATA_DIR, BASE_URL

DATE_FMT = "%Y %m %d"
TIME_FMT = "%H:%M"
DT_FMT = " ".join([DATE_FMT, TIME_FMT])


def get_show():
    # just a factory for a series with right index
    return pd.Series(index = [
            "title",
            "subtitle",
            "channel",
            "link",
            "start_time_raw",
            "start_dt",
            "end_dt",
            "duration",
        ]
    )


def get_raw_shows(channel, soup=None, verbose=True,
                  just_return_soup=False, return_df=True):
    """
    Return a list of the available shows from the passed channel dict
    of form:
        {'id': 143, 'name': 'Eurosport 1'}
    """

    if soup is None:
        url = BASE_URL + str(channel['id'])
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        if just_return_soup:
            return soup

    # dates are in h2 tags, contents in tr tags
    raw_list = soup.find_all(['h2', 'tr'])

    raw_shows = []
    curr_date = datetime.now().date()
    curr_date_raw = None

    for elem in raw_list:

        # set date_raw if this is an h2 element
        if elem.name == 'h2':
            curr_date_raw = elem.text
            date_out = curr_date.strftime(DATE_FMT)
            curr_date += timedelta(days=1)
            continue

        # check for a time str, which means its a show
        if not elem.find(attrs={'class': 'time'}):
            continue

        # otherwise gather the data
        if elem.name == 'tr':

            out = {
                'channel': channel['name'],
                'date_raw': curr_date_raw,
                'date_out': date_out,
                'time_raw': elem.find(attrs={'class': 'time'}).text,
                'title': elem.find(attrs={'class': 'title'}).text.strip(),
                'detail': (elem.find(attrs={'class': 'detail'}).text.strip()
                           .replace('/', ' - ')),
                'link': elem.find('a').get('href'),
            }

            raw_shows.append(tidy_raw_show(out))

            # if not first tr, go back and set the prev one's duration
            if len(raw_shows) > 1:
                dur_sec = ((raw_shows[-1]['start_dt']
                            - raw_shows[-2]['start_dt']).total_seconds())

                # this means it's a new day (raw_dt doesn't incr until 5am)
                if dur_sec < 0:
                    raw_shows[-1]['start_dt'] += timedelta(days=1)
                    dur_sec += 60 * 60 * 24

                raw_shows[-2]['duration'] = int(dur_sec / 60)
                raw_shows[-2]['end_dt'] = (raw_shows[-2]['start_dt']
                                        + timedelta(seconds=dur_sec))



    if verbose:
        print(f"Found {len(raw_shows)} shows for {channel['name']}")

    if raw_shows:
        return pd.concat(raw_shows, axis=1).T


def tidy_raw_show(raw_show):
    """
    Make a Show from raw show
    """

    show = get_show()

    show['channel'] = raw_show['channel']
    show['title'] = raw_show['title']
    show['subtitle'] = raw_show['detail']

    dt_raw = " ".join([raw_show['date_out'], raw_show['time_raw']])
    pm = dt_raw[-2:] == 'pm'

    show['start_dt'] = fix_dt_hours(
        datetime.strptime(dt_raw[:-2], DT_FMT), pm
    )

    show['start_time_raw'] = dt_raw

    return show


def fix_dt_hours(dt, pm, year=2020):
    """
    For a passed dt object, fix the hours based on whether pm flag
    """
    # add 12h unless is already 12.  And if exactly 12 pm, = 12

    if dt.hour == 12:
        # any 12:xx am should be 0:xx am
        if not pm:
            dt -= timedelta(hours=12)
            
    elif pm:
        dt += timedelta(hours=12)

    return dt


