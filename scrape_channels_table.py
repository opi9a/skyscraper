# skyscraper/scrape_channels_table.py

"""
Scripts for scraping the list of channels (with associated ids) from the
tvguide.co.uk site

Takes quite a while.  Not expected to be needed much.
"""

import requests
from bs4 import BeautifulSoup



def update_tv_guide_channels(channels_data_dir=None):
    """
    Run a scan for channels and update the list

    Not written or implemented, but this is what you'd do

    Channel list currently just as a dict hard pasted in skyscraper_constants
    """
    pass


def make_dict_from_raw_channels(raw_channels):
    """
    Take output from scan_channels, dump non channels and make a nice dict
    that can be saved to json
    """

    channels = [(c[0], c[1].split(" TV Listings")[0]) for c in raw_channels
                if c[1]]

    return [{'id': y[0], 'name': y[1]} for y in channels]


def scan_channels(start=0, stop=1500):
    """
    Return a list of tuples of channel id and name.
    This range was previously enough
    """

    channels = []

    for ch_id in range(start, stop):
        print(f'trying channel {ch_id:>4}..', end=' ')

        req = requests.get(BASE_URL + str(ch_id))
        if req.ok:
            print('ok', end= ' ')
            soup = BeautifulSoup(req.text, "html.parser")
            title = soup.title.text.strip()

            # if no channel, still get a return, like this
            if not title.startswith('TV Listings'):
                channels.append((ch_id, title))

            print(title)

        else:
            print('not found')
            channels.append((ch_id, None))
        
    return channels


