# skyscraper/skyscraper_constants.py

from pathlib import Path

from mylogger import get_timelog

# just use the dir the code is in
BASE_PATH = Path('.').absolute()
DATA_DIR = BASE_PATH / 'data/'

if not DATA_DIR.exists():
    print('making a directory at')
    DATA_DIR.mkdir(parents=True)
# LOG = get_timelog(BASE_PATH / 'logs/skyscraper.log.txt')

BASE_URL = "https://www.tvguide.co.uk/mobile/channellisting.asp?ch="
