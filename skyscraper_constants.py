# skyscraper/skyscraper_constants.py

from pathlib import Path

# just use the dir the code is in
BASE_PATH = Path(__file__).parent.absolute()
DATA_DIR = BASE_PATH / 'data/'

try:
    from mylogger import get_timelog
    LOG = get_timelog(BASE_PATH / 'logs/skyscraper.log')

except:
    class NullLog:
        def info(self, log_string): pass
    LOG = NullLog()

if not DATA_DIR.exists():
    print('making a directory at')
    DATA_DIR.mkdir(parents=True)

BASE_URL = "https://www.tvguide.co.uk/mobile/channellisting.asp?ch="
