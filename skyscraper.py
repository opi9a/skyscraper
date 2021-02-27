# skyscraper/skyscraper.py

import argparse

from skyscraper_constants import LOG
from Schedule import Schedule

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        epilog=('show tv listings for set of channels'
                '\nadd terms to filter')
    )

    parser.add_argument('include_strings', nargs='*', type=str,
                        help='provide string to filter title and subtitle by')

    parser.add_argument('-x', '--exclude-strings', nargs='+', type=str,
                        help='tags to filter shows out')

    parser.add_argument('-r', '--reverse', action='store_true',
                        help='print in descending date')

    parser.add_argument('-k', '--keep-duplicates', action='store_true',
                        help='keep show listings that seem to be duplicates on '
                             'different channels at the same time')

    parser.add_argument('-u', '--force-update', action='store_true',
                        help='force update even if scrape done today')

    parser.add_argument('-c', '--group-by-channel', action='store_true',
                        help='group listings by channel rather than day')

    parser.add_argument('-e', '--group-by-show', action='store_true',
                        help='group listings by show rather than day')

    parser.add_argument('-d', '--days-to-show', default=1, type=int,
                        help='number of days hence to show [default=1]')

    parser.add_argument('-w', '--whole-week', action='store_true',
                        help='display shows for whole week - overrides "-d"')

    parser.add_argument('-l', '--lines-per-show', default=1, type=int,
                        help='number of lines to use per show [default=1]')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print up to 10 lines per show - overrides "-l"')

    parser.add_argument('-o', '--keep-finished-shows', action='store_true',
                        help='do not discard shows whose end time has passed')

    parser.add_argument('-s', '--get-synchronously', action='store_true',
                        help='do not fetch show data asynchronously')

    parser.add_argument('-m', '--mute', action='store_true',
                        help='do not print any output (eg if just updating)')

    args = parser.parse_args()

    if args.whole_week:
        no_days = 7
    else:
        no_days = args.days_to_show

    if args.verbose:
        max_show_rows = 10
    else:
        max_show_rows = args.lines_per_show

    if args.group_by_channel:
        group_by = 'channel'
    elif args.group_by_show:
        group_by = 'show'
    else:
        group_by = 'day'

    schedule = Schedule(update_todays=args.force_update,
                        drop_duplicates=not(args.keep_duplicates),
                        include_strings=args.include_strings,
                        exclude_strings=args.exclude_strings,
                        group_by=group_by,
                        no_days=no_days, get_async=not(args.get_synchronously),
                        remove_shows_over=not(args.keep_finished_shows))

    if not args.mute:
        schedule.print_df(reverse=args.reverse, max_rows=max_show_rows)


