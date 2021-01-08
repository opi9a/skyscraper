# skyscraper/skyscraper.py

import argparse

from Schedule import Schedule

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('filter_strings', nargs='+', type=str,
                        help='provide string to filter title and subtitle by')

    parser.add_argument('-x', '--exclude-strings', nargs='+', type=str,
                        help='tags to filter out')

    parser.add_argument('-r', '--reverse', action='store_true',
                        help='print in descending date')

    parser.add_argument('-k', '--keep-duplicates', action='store_true',
                        help='print in descending date')

    parser.add_argument('-u', '--force-update', action='store_true',
                        help='force update even if scrape done today')

    parser.add_argument('-c', '--group-by-channel', action='store_true',
                        help='group listings by channel rather than day')

    parser.add_argument('-d', '--days-to-show', default=None, type=int,
                        help='group listings by channel rather than day')

    parser.add_argument('-l', '--lines-per-show', default=1, type=int,
                        help='number of lines to use per show')

    args = parser.parse_args()

    schedule = Schedule(update_todays=args.force_update,
                        drop_duplicates=not(args.keep_duplicates),
                        filter_strings=args.filter_strings,
                        exclude_strings=args.exclude_strings,
                        no_days=args.days_to_show)

    schedule.print_df(reverse=args.reverse, max_rows=args.lines_per_show)


