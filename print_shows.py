
import time
from datetime import datetime
from collections import OrderedDict
from os import get_terminal_size
from termcolor import cprint, colored
# from skyscraper_constants import LOG

FIELDS_TO_PRINT = ['channel', 'day', 'title', 'subtitle', 'start_time_str', 'end_time_str']

BASE_COL_WIDTHS = {
    # only the fixed ones, others looked up
    'title': None,
    'subtitle': None,
    'c_day': 8, # Wed 28th
    'c_channel': 8, # Sky Main
    'start_time_str': 5, # 16:30
    'end_time_str': 5, # 17:30
}

SUB_MAIN_RATIO = 3 # ratio of width of subtitle and title columns
MAX_SHOW_ROWS = 5
MAX_SCREEN_WIDTH = 110
SCREEN_LINES = 135

LONG_DAY_FMT = "%A %d %B"
SHORT_DAY_FMT = "%a %d"

SCROLL_SLEEP_TIME = 0.003


def print_df(df, col_widths=None, group_by='long_day',
             screen_width=None, max_show_rows=None,
             screen_lines=None):
    """
    Print the df, splitting by channel or day
    """
    screen_width = min(
        MAX_SCREEN_WIDTH,
        screen_width or get_terminal_size()[0] - 4
    )

    max_show_rows = max_show_rows or MAX_SHOW_ROWS

    screen_lines = screen_lines or get_terminal_size()[1] - 4

    if col_widths is None:
        max_lens = get_max_lens(df)
        col_widths = get_col_widths(max_lens, screen_width)

    headings = df[group_by].unique()

    rows_printed = 0

    for heading in headings:
        pad1 = int((screen_width - len(heading)) / 2)
        pad2 = screen_width - len(heading) - pad1 + 1
        print()
        print('-' * pad1, end = ' ')
        cprint(heading, attrs=['bold'], end=' ')
        print('-' * pad2, end='')

        rows_printed = print_end(rows_printed, screen_lines)

        if max_show_rows > 1:
            rows_printed = print_end(rows_printed, screen_lines)

        sub_df = df.loc[df[group_by] == heading]

        for i in range(len(sub_df)):
            rows_printed = print_show(
                sub_df.iloc[i], col_widths, group_by=group_by,
                max_show_rows=max_show_rows, rows_printed=rows_printed,
                screen_lines=screen_lines
            )

    rows_printed = print_end(rows_printed, screen_lines)


def print_show(show, col_widths, group_by='long_day', max_show_rows=None,
               rows_printed=None, screen_lines=SCREEN_LINES):
    """
    Given col_widths, print the show.  Group by channel or long_day
    """

    max_show_rows = max_show_rows or MAX_SHOW_ROWS

    # TODO if only 1 row just print all chars possible

    col_widths = col_widths.copy()

    del col_widths['c_channel' if group_by == 'channel' else 'c_day']

    # want a dict, keys are fields, vals are lists of strings for each line
    by_line = {}

    for field in col_widths:
        if field in ['title', 'subtitle']:
            by_line[field] = split_line(show[field], col_widths[field])
        else:
            by_line[field] = [show[field]]

    max_lines = min(
        max_show_rows,
        len(max(by_line.values(), key=lambda x: len(x)))
    )

    # iterate over the lines in each field
    for i in range(max_lines):
        for field, lines in by_line.items():
            pad = col_widths[field]
            if field == 'title':
                print(' ', end='')
            if i == 0 and not lines[i]:
                print('-'.ljust(pad), end='')
            elif i < len(lines):
                print(lines[i].ljust(pad), end=' ')
            else:
                print("".ljust(pad), end=' ')

        if max_show_rows > 1:
            rows_printed = print_end(rows_printed, screen_lines)

    rows_printed = print_end(rows_printed, screen_lines)

    time.sleep(SCROLL_SLEEP_TIME)

    return rows_printed


def print_end(rows_printed, screen_lines):
    """
    Print an empty line to end a row, then test for pagination
    """

    print()
    rows_printed += 1

    if rows_printed >= screen_lines:
        cprint('<press return to continue>', color='green', end="")
        _ = input('')
        return 0

    return rows_printed


def get_max_lens(df):
    """
    Return the max length across each field in the passed shows
    """

    # set up empty dict for the variable fields
    out = BASE_COL_WIDTHS.copy()

    for field in ['title',  'subtitle', 'c_channel', 'c_day']:
        out[field] = max(df[field].apply(len)) 

    return out


def get_col_widths(max_lens, term_size, sub_main_ratio=None):
    """
    Return the col_widths to use
    Only title and subtitle to vary
    (max_lens dict will have c_day and c_channel, both not needed, but same size)
    """
    sub_main_ratio = sub_main_ratio or SUB_MAIN_RATIO

    # work out cols taken by invariants
    # ignore c_channel, as one of it or c_day (same size) will be excluded
    pad = 1
    const_widths_sum = sum(v + pad for k, v in BASE_COL_WIDTHS.items()
                           if k in ['c_day', 'start_time_str', 'end_time_str'])

    cols_avail = term_size - const_widths_sum

    out = BASE_COL_WIDTHS.copy()
    out['title'] = min(int(cols_avail / sub_main_ratio), max_lens['title'])
    out['subtitle'] = min(cols_avail - out['title'], max_lens['subtitle'])

    return out


def split_line(line, max_width):
    """
    Return a list with the input line split to fit the max_width
    """

    # go through the line, stopping at last spaces before max_width


    out = [""]

    for word in line.split():
        # if the new word would overshoot, start a new line
        if len(word) + len(out[-1]) >= max_width:
            out.append(word)
        else:
            out[-1] = " ".join([out[-1], word])

    out[0] = out[0].strip()

    return out



def print_shows(shows, sort_by='channel'):
    """
    Just print a list of shows on command line.  Choose div by channel or day.

    Cols:
        Channel OR day / title / subtitle / time / dur?

    If by channel / day, print a line for channel / day before each group
    """
    
    shows.sort(key = lambda x:x[sort_by])

    div_name = None
    pad = 8

    for show in shows:
        if show[sort_by] != div_name:
            if sort_by == 'day':
                cprint("\n" + show[sort_by].strftime("%A %d %b"), attrs=['bold'])
            else:
                cprint("\n" + show[sort_by], attrs=['bold'])

            div_name = show[sort_by]

        else:
            for field in FIELDS_TO_PRINT:
                if field == sort_by:
                    continue
                elif field == 'day':
                    print(show['start_time_str'].strftime("%a"), end=" ")

                elif field.endswith('dt'):
                    try:
                        print(show[field].strftime("%H:%M").ljust(pad), end=" ")
                    except:
                        print('N/A'.ljust(pad), end=" ")

                else:
                    print(show[field][:pad].ljust(pad), end=" ")

            print("")



    # if log is not None:
    #     log.info("new call to print games")

    # term_cols = get_terminal_size()[0]

    # pad2, pad3 = 28, 12

    # pad1 = term_cols - pad2 - (pad3 * 2) - 3

    # for i, day in enumerate(shows):
    #     if i == days:
    #         break

    #     print("")
    #     cprint(" " + shows[day]['day'], attrs=['bold'])
    #     print("")

    #     # avoid duplicates (may be different channels)
    #     games_printed = set()

    #     games_to_print = shows[day]['games']

    #     if by_title:
    #         games_to_print = sorted(games_to_print, key=lambda x: x['title'])

    #     last_title = None

    #     for game in games_to_print:

    #         out_str = "".join([
    #             game['title'][:pad1].ljust(pad1),
    #             game['channel'].split()[0][:pad2].rjust(pad2),
    #             game['type'][:pad3].rjust(pad3),
    #             game['time'][:pad3].rjust(pad3)
    #         ])

    #         if last_title is not None and game['title'] != last_title:
    #             out_str = "\n "+ out_str 

    #         if out_str not in games_printed:
    #             print(" " + out_str)
    #             games_printed.add(out_str)

    #         if by_title:
    #             last_title = game['title']

    # if log is not None:
    #     log.info("finished printing games")


