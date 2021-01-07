# skyscraper/tv_guide.py

from pathlib import Path
import json
from datetime import datetime

from skyscraper_constants import DATA_DIR
from Show import Show
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

class Schedule():

    def __init__(self, channels=None, data_dir=None,
                 channels_json_fp=None,
                 update_todays=False, save_shows=True,
                 raw_shows=None):
        """
        Get listings for the channels, save to data_dir


        """

        # first check if there is a scrape saved today already
        data_dir = data_dir or DATA_DIR
        self.date_str = datetime.now().strftime(DATE_FMT)
        self.save_fp = DATA_DIR / "".join([DAILY_PREFIX, self.date_str, '.json'])

        if raw_shows is not None:
            self.raw_shows = raw_shows

        elif not update_todays and self.save_fp in list(data_dir.iterdir()):
            print('found saved shows for today,', self.date_str)

            self.from_json()


        else:

            # input is a list of channel names
            channels = channels or CHANNELS

            # need a dict of keys id, name for each
            self.channels_table = [x for x in get_channels_table()
                                   if x['name'] in channels]

            # raw_shows is just a list, not organised
            self.raw_shows = []

            for channel in self.channels_table:
                self.raw_shows.extend(get_raw_shows(channel))

            if save_shows:
                self.to_json()


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
            for show in self.raw_shows:
                if target.lower() in show[field].lower():
                    print('matched', target, 'in', show[field].lower())
                    selected.append(show)
                    print('now have', len(selected), 'shows')

        
        self.shows_selection = sorted(selected, key= lambda x: x[self.sort_by])



    def from_json(self, load_path=None):
        """
        Load shows as dicts and convert
        """

        load_path = load_path or self.save_fp

        with open(load_path, 'r') as fp:
            show_dicts = json.load(fp)

        for show_dict in show_dicts:
            for dt in ['start_dt', 'end_dt']:
                if show_dict[dt] is not None:
                    show_dict[dt] = datetime.fromisoformat(show_dict[dt])

        self.raw_shows = [Show(show_dict=s) for s in show_dicts]


    def to_json(self, save_path=None):
        """
        Convert the shows and save them
        """

        save_path = save_path or self.save_fp

        with open(save_path, 'w') as fp:
            json.dump([x.__dict__ for x in self.raw_shows], fp,
                      default=str, indent=4)

        print('saved shows to', save_path)


