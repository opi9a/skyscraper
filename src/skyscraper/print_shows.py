
import pandas as pd
import readchar
import time
from datetime import datetime
from collections import OrderedDict
from os import get_terminal_size
from termcolor import cprint, colored
# from constants import LOG

FIELDS_TO_PRINT = ['channel', 'long_day', 'title', 'subtitle',
                   'start_time_str', 'end_time_str']
"""
group_by:
    channel:
        segment by channel


"""
SCHEMAS = { 
    'channel': {
        'segment_heading': 'channel',
        'sort_by': 'start_dt',
        'fields': ['title', 'subtitle', 'c_day', 'start_time_str', 'end_time_str']
    },

    'day': {
        'segment_heading': 'long_day',
        'sort_by': 'start_dt',
        'fields': ['title', 'subtitle', 'c_channel', 'start_time_str', 'end_time_str']
    },

    'show': {
        'segment_heading': 'title',
        'sort_by': 'start_dt',
        'fields': ['subtitle', 'agg_channels', 'agg_days',
                   'agg_start_str', 'agg_end_str']
    },
}

LINKER = '<BR>'

INVARIANT_COL_WIDTHS = {
    'c_day': 8, # Wed 28th
    'c_channel': 8, # Sky Main
    'start_time_str': 5, # 16:30
    'end_time_str': 5, # 17:30
    'agg_days': 8, # Wed 28th
    'agg_channels': 8, # Sky Main
    'agg_start_str': 5, # 16:30
    'agg_end_str': 5, # 17:30
}

SUB_MAIN_RATIO = 3 # ratio of width of subtitle and title columns
MAX_SHOW_ROWS = 5
MAX_SCREEN_WIDTH = 110
SCREEN_LINES = 135

LONG_DAY_FMT = "%A %d %B"
SHORT_DAY_FMT = "%a %d"

SCROLL_SLEEP_TIME = 0.003


def make_df_by_show(df):
    """
    Compress df such that each show (based on title and subtitle combination)
    has a single line - with multiple showings represented as extended strings
    in fields 'agg_channels', 'agg_days', 'agg_start_str', 'agg_end_str'
    """

    df = df.copy().sort_values(['title', 'subtitle', 'start_dt'])

    # get the unique_shows, identified by title, subtitle tuple
    unique_shows = tuple(df.set_index(['title', 'subtitle']).index.unique())


    # use the global linker to join listings eg for channel
    # - will split by this later when turning into multiple rows for printing
    linker = LINKER

    # iterate over the unique_shows, adding to a list of series with processed
    # shows
    shows_list = []
    for show in unique_shows:
        sub_df = df.loc[(df.title == show[0])
                        & (df.subtitle == show[1])]

        show_dict = {
            'title': show[0],
            'subtitle': show[1],
            'duration': sub_df.duration.unique()[0],
            'agg_channels': linker.join(sub_df.c_channel.values),
            'agg_days': linker.join(sub_df.c_day.values),
            'agg_start_str': linker.join(sub_df.start_time_str.values),
            'agg_end_str': linker.join(sub_df.end_time_str.values),
        }

        shows_list.append(pd.Series(show_dict))

    return pd.concat(shows_list, axis=1).T


def print_df(df, col_widths=None, group_by='day',
             screen_width=None, max_show_rows=None,
             screen_lines=None):
    """
    Print the df, splitting into groups of rows according to group_by
    """
    screen_width = min(
        MAX_SCREEN_WIDTH,
        screen_width or get_terminal_size()[0] - 4
    )

    max_show_rows = max_show_rows or MAX_SHOW_ROWS

    screen_lines = screen_lines or get_terminal_size()[1] - 6

    cols_to_print = SCHEMAS[group_by]['fields']
    segment_heading = SCHEMAS[group_by]['segment_heading']

    # dev need this to reflect schema
    if col_widths is None:
        max_lens = get_max_lens(df)
        # needs to depend on schema (fields)
        col_widths = get_col_widths(max_lens, cols_to_print, screen_width)

    headings = df[segment_heading].unique()

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

        sub_df = df.loc[df[segment_heading] == heading]

        for i in range(len(sub_df)):
            rows_printed = print_show(
                sub_df.iloc[i], col_widths, 
                max_show_rows=max_show_rows, rows_printed=rows_printed,
                screen_lines=screen_lines
            )

    rows_printed = print_end(rows_printed, screen_lines)


def print_show(show, col_widths, max_show_rows=None,
               rows_printed=None, screen_lines=SCREEN_LINES):
    """
    Given col_widths, print the show.  Group by channel or long_day
    """

    max_show_rows = max_show_rows or MAX_SHOW_ROWS

    # TODO if only 1 row just print all chars possible

    col_widths = col_widths.copy()

    # want a dict, keys are fields, vals are lists of strings for each line
    by_line = {}

    for field in col_widths:
        if field in ['title', 'subtitle']:
            by_line[field] = split_line(show[field], col_widths[field])
        else:
            by_line[field] = [show[field]]

    # split any elements with LINKER
    is_agg_show = False
    for field, value in by_line.items():
        if LINKER in value[0]:
            by_line[field] = value[0].split(LINKER)
            is_agg_show = True

    # if the invariant fields are aggregates split over multiple lines, use
    # these to set the max lines
    if is_agg_show:
        max_lines = len(by_line['agg_days'])

    else:
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
        cprint('<press q to stop this happening or any other key to continue> ',
               color='green', end="", flush=True)

        x = readchar.readchar()

        if x == 'q':
            print()
            raise SystemExit

        else:
            print()
            return 0

    return rows_printed


def get_max_lens(df):
    """
    Return the max length across each field in the passed shows
    """

    # set up empty dict for the variable fields
    out = INVARIANT_COL_WIDTHS.copy()

    for field in df.columns:
        try:
            out[field] = max(df[field].apply(len)) 
        except:
            pass

    return out


def get_col_widths(max_lens, cols_to_print, term_size,
                       sub_main_ratio=None):
    """
    Take dict of max lens, and the cols to be printed
    Return the col_widths to use
    Only title and subtitle to vary
    """
    sub_main_ratio = sub_main_ratio or SUB_MAIN_RATIO

    # get skeleton output, with invariants

    out = {
        field: INVARIANT_COL_WIDTHS.get(field, None)
        for field in cols_to_print
    }

    # work out cols taken by invariants
    pad = 1

    const_widths_sum = sum(width + pad for width in out.values()
                           if width is not None)

    # now split remainder between title and subtitle
    cols_avail = term_size - const_widths_sum

    # subtitle always printed. If title reqd, split, otherwise all to subtitle
    if 'title' in cols_to_print:
        out['title'] = min(int(cols_avail / sub_main_ratio), max_lens['title'])
        out['subtitle'] = min(cols_avail - out['title'], max_lens['subtitle'])

    else:
        out['subtitle'] = cols_avail
    
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



