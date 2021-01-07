
from pathlib import Path
import getpass

from mylogger import get_timelog

USER = getpass.getuser()
BASE_PATH = Path('/home/' + USER + '/shared/projects/skyscraper/')
DATA_DIR = BASE_PATH / 'data/tv_guide/'
LOG = get_timelog(BASE_PATH / 'logs/skyscraper.log.txt')

