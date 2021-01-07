# skyscraper/tv_guide.py

from pathlib import Path
import json
from datetime import datetime
import pandas as pd

from skyscraper_constants import DATA_DIR
from scrape_tv_guide import get_channels_table, get_raw_shows

"""
Scripts to scrape listings from the tv_guide.co.uk site

Also functions to scrape the channel list - may be needed now and then
"""


CHANNELS = ['Eurosport 1',
            'Eurosport 2',
            'Sky Sports NFL',
            'Sky Sports Main Event',
            'Sky Sports Mix',
           ]

# format for saving to disk
DAILY_PREFIX = "tvg_raw_shows_"
DATE_FMT = "%Y-%m-%d"

# for printing
LONG_DAY_FMT = "%A %d %B"
SHORT_DAY_FMT = "%a %d"
TIME_FMT = "%H:%M"


class Schedule():

    def __init__(self, channels=None, data_dir=None,
                 update_todays=False, save_shows=True,
                 df=None):
        """
        Get listings for the channels, save to data_dir
        """

        # first check if there is a scrape saved today already
        data_dir = data_dir or DATA_DIR
        self.date_str = datetime.now().strftime(DATE_FMT)
        self.save_fp = DATA_DIR / "".join([DAILY_PREFIX, self.date_str, '.csv'])

        if df is not None:
            self.df = df

        elif not update_todays and self.save_fp in list(data_dir.iterdir()):
            print('found saved shows for today,', self.date_str)

            self.df = pd.read_csv(self.save_fp, index_col=0)
            print('loaded from', self.save_fp)


        else:

            # input is a list of channel names
            channels = channels or CHANNELS

            # need a dict of keys id, name for each
            self.channels_table = [x for x in get_channels_table()
                                   if x['name'] in channels]

            # df is best to store this
            df = pd.concat([get_raw_shows(channel)
                            for channel in self.channels_table])

            df['c_channel'] = df.channel.apply(compress_channel)
            df['c_day'] = df.start_dt.apply(compress_day)
            df['long_day'] = df.start_dt.dt.strftime(LONG_DAY_FMT)
            df['start_time_str'] = df.start_dt.dt.strftime(TIME_FMT)
            df['end_time_str'] = df.end_dt.dt.strftime(TIME_FMT)

            self.df = df.fillna('NA')

            if save_shows:
                self.df.to_csv(self.save_fp)
                print('saved to', self.save_fp)


        # filtering. set up strings for each filterable field
        # title subtitle channel
        # and something for day
        # also allow sorting
        # have an attr for the processed list and a method for display
        # modify the filters, set sorting etc, then display results
        self.filter_strings = {
            'title': None,
            'subtitle': None,
            'channel': None,
            'weekday': None,
        }

        self.sort_by = 'channel' # or 'start_dt'

        self.shows_selection = None


    def apply(self):
        """
        apply the filters and sorting strategy to generate a new
        shows_selection attribute
        """
        selected = []

        for field, target in self.filter_strings.items():
            print('with field', field, 'target', target)
            if target is None:
                continue
            for show in self.df:
                if target.lower() in show[field].lower():
                    print('matched', target, 'in', show[field].lower())
                    selected.append(show)
                    print('now have', len(selected), 'shows')

        
        self.shows_selection = sorted(selected, key= lambda x: x[self.sort_by])


DAY_SUFFIXES = { 1: 'st', 2: 'nd', 3: 'rd',
                21: 'st', 22: 'nd', 23: 'rd', 31: 'st'}

def compress_day(dt):
    """
    From datetime obj, get day in format Thu 9th
    """

    out =  "".join([
        dt.strftime(SHORT_DAY_FMT),
        DAY_SUFFIXES.get(dt.day, 'th')
    ])

    return out.replace(' 0', ' ')


def compress_channel(channel_name):
    """
    Make a compressed version
    """

    channel_name = channel_name.replace('Sky Sports', 'Sky')
    channel_name = channel_name.replace('Eurosport', 'Eur')
    channel_name = channel_name.replace(' Event', '')

    return channel_name



