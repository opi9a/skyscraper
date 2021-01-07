
from datetime import datetime
from collections import OrderedDict
from os import get_terminal_size
from termcolor import cprint, colored
from skyscraper_constants import LOG

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



LONG_DAY_FMT = "%A %d %B"
SHORT_DAY_FMT = "%a %d"

class Printer():
    """
    Object to hold printing info and do the printing

    if channel:
        title, subtitle, c_day, start, end

    if day:
        title, subtitle, c_channel, start, end

    1. df
    2. work out max col widths (have this already?)
    3. list of channels or days
    4. for each:
        get df selection eg df.loc['channel' == channel]
        print title eg Sky Sports Mix
        for each row
    2. get column widths for fields to print:
        - channel or day
        - 'title', 'subtitle', ['c_channel' or 'c_day'] 'start_time_str', 'end_time_str'
        - 'c_day' and 'c_channel' are day and channel in compressed format

    3. get justified entries, one dict per show:
        - field names as keys
        - list of strings as values, each string a line to print
          for that field

    4. do the actual printing
    """

    def __init__(self, df, group_by='channel', max_show_rows=10):

        self.df = df
        self.max_lens = get_max_lens(df) # lengths of show fields
        self.col_widths = get_col_widths(self.max_lens, get_terminal_size()[0])


def print_show(show, col_widths, to_skip='c_day'):
    """
    Given col_widths, print the show
    """

    col_widths = col_widths.copy()
    del col_widths[to_skip]

    # want a dict, keys are fields, vals are lists of strings for each line
    by_line = {}

    for field in col_widths:
        if field in ['title', 'subtitle']:
            by_line[field] = split_line(show[field], col_widths[field])
        else:
            by_line[field] = [show[field]]

    max_lines = len(max(by_line.values(), key=lambda x: len(x)))

    for i in range(max_lines):
        for field, lines in by_line.items():
            if i < len(lines):
                print(lines[i].ljust(col_widths[field]), end=' ')
            else:
                print("".ljust(col_widths[field]), end=' ')

        print()

    print()



    # pass


def get_max_lens(df):
    """
    Return the max length across each field in the passed shows
    """

    # set up empty dict for the variable fields
    out = BASE_COL_WIDTHS.copy()

    for field in ['title',  'subtitle', 'c_channel', 'c_day']:
        out[field] = max(df[field].apply(len)) 

    return out


def get_col_widths(max_lens, term_size):
    """
    Return the col_widths to use
    Only title and subtitle to vary
    (max_lens dict will have c_day and c_channel, both not needed, but same size)
    """
    # work out cols taken by invariants
    # ignore c_channel, as one of it or c_day (same size) will be excluded
    pad = 1
    const_widths_sum = sum(v + pad for k, v in BASE_COL_WIDTHS.items()
                           if k in ['c_day', 'start_time_str', 'end_time_str'])

    cols_avail = term_size - const_widths_sum

    sub_main_ratio = 3
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



def print_shows(shows, sort_by='channel', log=LOG):
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


