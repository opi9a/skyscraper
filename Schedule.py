# skyscraper/tv_guide.py

from pathlib import Path
import json
from datetime import datetime
import pandas as pd
from termcolor import cprint
from concurrent.futures import ThreadPoolExecutor

from skyscraper_constants import DATA_DIR, LOG
from scrape_tv_guide import get_raw_shows
from print_shows import print_df

"""
Object and scripts to scrape listings from the tv_guide.co.uk site
"""

# this is a subset of full list - see channels/channels.json
# (and scrape_channels_table.py to regenerate it)
CHANNELS = [
    {'id': 142, 'name': 'Eurosport 1'},
    {'id': 400, 'name': 'Eurosport 2'},
    {'id': 1094, 'name': 'Sky Sports NFL'},
    {'id': 1104, 'name': 'Sky Sports Main Event'},
    {'id': 1106, 'name': 'Sky Sports Mix'}
]


# formats for saving to disk
DAILY_PREFIX = "tvg_raw_shows_"
DATE_FMT = "%Y-%m-%d"

# formats for printing
LONG_DAY_FMT = "%A %d %B"
SHORT_DAY_FMT = "%a %d"
TIME_FMT = "%H:%M"

MAX_SCREEN_WIDTH = 120


class Schedule():

    def __init__(self, print_df=False, reverse=True,
                 drop_duplicates=True, by_channel=False,
                 channels=None, data_dir=None,
                 update_todays=False, save_shows=True,
                 include_strings=None, exclude_strings=None, no_days=None,
                 remove_shows_over=True, get_async=True,
                 log=LOG):
        """
        Load or scrape a df of channels
        Apply filters
        Print nice
        """

        # set up some attributes
        data_dir = data_dir or DATA_DIR
        self.date_str = datetime.now().strftime(DATE_FMT)
        self.save_fp = DATA_DIR / "".join([DAILY_PREFIX, self.date_str, '.csv'])
        self.include_strings = include_strings or None
        self.exclude_strings = exclude_strings or None
        self.by_channel = by_channel
        self.no_days = no_days or None
        self.remove_shows_over = remove_shows_over
        

        # check if there is a scrape saved today already
        if not update_todays and self.save_fp in list(data_dir.iterdir()):
            self.df = pd.read_csv(self.save_fp, index_col=0, 
                                 parse_dates=['start_dt', 'end_dt'])
            LOG.info(f'loaded existing df from {self.save_fp}')

        # else scrape a df
        else:
            LOG.info(f'beginning new scrape')

            # need a list of channel dicts, with id, name for each
            self.channels_table = channels or CHANNELS

            if get_async:
                with ThreadPoolExecutor() as conn:
                    shows_generator = conn.map(get_raw_shows,
                                               self.channels_table)
            else:
                shows_generator = [get_raw_shows(channel)
                                   for channel in self.channels_table]

            df = pd.concat(shows_generator)

            df.index=pd.RangeIndex(0, len(df.index))

            df = df.sort_values('start_dt')

            df['c_channel'] = df.channel.apply(compress_channel)
            df['c_day'] = df.start_dt.apply(compress_day)
            df['long_day'] = df.start_dt.dt.strftime(LONG_DAY_FMT)
            df['start_time_str'] = df.start_dt.dt.strftime(TIME_FMT)
            df['end_time_str'] = df.end_dt.dt.strftime(TIME_FMT)

            self.df = df

            if save_shows:
                self.df.to_csv(self.save_fp)
                print('saved to', self.save_fp)

            LOG.info(f'finished scrape, found {len(df)} shows')


        # make the filtered view
        self.df_filtered = self.df

        if include_strings is not None or no_days is not None:
            self.apply(drop_duplicates=drop_duplicates)

        if print_df:
            self.print_df(reverse=reverse, by_channel=self.by_channel)


    def apply(self, df=None, include_strings=None, exclude_strings=None,
              no_days=None, return_df=False, drop_duplicates=True,
              remove_shows_over=None, by_channel=False):
        """
        Apply the current include_strings  and no_days to the full df
        """

        if df is None:
            df = self.df

        if drop_duplicates:
            df = df.drop_duplicates(subset=['subtitle', 'start_dt'],
                                    keep='first')

        no_days = no_days or self.no_days
        include_strings = include_strings or self.include_strings
        exclude_strings = exclude_strings or self.exclude_strings
        remove_shows_over = remove_shows_over or self.remove_shows_over
        by_channel = by_channel or self.by_channel

        if no_days is not None:
            days = df['c_day'].unique()[:no_days]
            df = df.loc[df['c_day'].isin(days)]

        if include_strings is not None:
            df = dfilter(df, include_strings)

        if exclude_strings is not None:
            df = dfilter(df, exclude_strings, exclude=True)

        if remove_shows_over:
            df = df.loc[~(df.end_dt < datetime.now())]

        df = df.fillna('NA')

        if by_channel:
            df = df.sort_values(['channel', 'start_dt'])

        if return_df:
            return df
        else:
            if df is not None:
                self.df_filtered = df
            else:
                self.df_filtered = pd.DataFrame(columns=self.df.columns)



    def print_df(self, reverse=False, by_channel=None,
                 max_rows=None):
        """
        print the filtered df
        """

        if by_channel is None:
            by_channel = self.by_channel

        if by_channel:
            group_by = 'channel'
        else:
            group_by = 'long_day'

        if not len(self.df_filtered):
            print('nothing found with filter:', end=' ')
            cprint("+ " + ", ".join(self.include_strings), color='green', end=' ')
            cprint("- " + ", ".join(self.exclude_strings), color='red')
            return

        if reverse:
            print_df(self.df_filtered.sort_index(ascending=False),
                     group_by=group_by, max_show_rows=max_rows)

        else:
            print_df(self.df_filtered, group_by=group_by,
                     max_show_rows=max_rows)

        print(f' [ {len(self.df_filtered)} / {len(self.df)} shows for terms:', end=" ")
        if self.include_strings is not None:
            cprint("+ " + ", ".join(self.include_strings), color='green', end=' ')
        if self.exclude_strings is not None:
            cprint("- " + ", ".join(self.exclude_strings), color='red', end=' ')

        if self.no_days == 1:
            print(f'over 1 day', end=' ')
        else:
            print(f'over {self.no_days} days', end=' ')

        print(']')


def dfilter(df, strings, exclude=False):
    """
    Return a view of the df filtered by the passed string
    vs title and subtitle fields
    """

    mask = True

    for string in strings:

        string = string.lower()

        condition = (df['title'].str.lower().str.contains(string)
                     | df['subtitle'].str.lower().str.contains(string))

        if not exclude:
            mask &= condition

        else:
            mask &= ~condition

    return df.loc[mask]



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



