# skyscraper/skyscraper.py

import argparse

from skyscraper_constants import LOG
from Schedule import Schedule

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        epilog=('show tv listings for set of channels'
                '\nadd terms to filter')
    )

    parser.add_argument('include_strings', nargs='+', type=str,
                        help='provide string to filter title and subtitle by')

    parser.add_argument('-x', '--exclude-strings', nargs='+', type=str,
                        help='tags to filter out')

    parser.add_argument('-r', '--reverse', action='store_true',
                        help='print in descending date')

    parser.add_argument('-k', '--keep-duplicates', action='store_true',
                        help='keep show listings that seem to be duplicates on '
                             'different at the same time')

    parser.add_argument('-u', '--force-update', action='store_true',
                        help='force update even if scrape done today')

    parser.add_argument('-c', '--group-by-channel', action='store_true',
                        help='group listings by channel rather than day')

    parser.add_argument('-d', '--days-to-show', default=1, type=int,
                        help='group listings by channel rather than day')

    parser.add_argument('-l', '--lines-per-show', default=1, type=int,
                        help='number of lines to use per show')

    parser.add_argument('-o', '--keep-shows-over', action='store_true',
                        help='do not discard shows whose end time has passed')

    args = parser.parse_args()

    schedule = Schedule(update_todays=args.force_update,
                        drop_duplicates=not(args.keep_duplicates),
                        include_strings=args.include_strings,
                        exclude_strings=args.exclude_strings,
                        no_days=args.days_to_show,
                        remove_shows_over=not(args.keep_shows_over))

    schedule.print_df(reverse=args.reverse, max_rows=args.lines_per_show)


