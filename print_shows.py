
from datetime import datetime
from collections import OrderedDict
from os import get_terminal_size
from termcolor import cprint, colored
from skyscraper_constants import LOG

FIELDS_TO_PRINT = ['channel', 'day', 'title', 'subtitle', 'start_dt', 'end_dt']

BASE_COL_WIDTHS = {
    # only the fixed ones, others looked up
    'day': 8, # Wed 28th
    'start_dt': 5, # 16:30
    'end_dt': 5, # 17:30
}

LONG_DAY_FMT = "%A %d %B"
SHORT_DAY_FMT = "%a %d"

class Printer():
    """
    Object to hold printing info and do the printing

    1. make dict by group_by field ('channel', 'day')
    2. get column widths for fields to print:
        - channel or day
        - 'title', 'subtitle', ['c_channel' or 'c_day'] 'start_dt', 'end_dt'
        - 'c_day' and 'c_channel' are day and channel in compressed format

    3. get justified entries, one dict per show:
        - field names as keys
        - list of strings as values, each string a line to print
          for that field

    4. do the actual printing
    """

    def __init__(self, shows, group_by='channel', max_show_rows=10):

        # make dicts with keys of group_by field, vals of show lists
        if group_by == 'channel':
            # show['c_day'] = show['start_dt'].strftime(SHORT_DAY_FMT)
            shows = [{
                'title': show['title'],
                'subtitle': show['subtitle'],
                'channel': show['channel'],
                'start_dt': show['start_dt'],
                'end_dt': show['end_dt'],
                'c_day': show['start_dt'].strftime(SHORT_DAY_FMT)
            } for show in shows]

            channels = {show['channel'] for show in shows}
            self.shows = {channel: [] for channel in channels}

            for show in shows:
                self.shows[show['channel']].append(show)

        elif group_by == 'day':

            shows = [{
                'title': show['title'],
                'subtitle': show['subtitle'],
                'c_channel': compress_channel(show['channel']),
                'start_dt': show['start_dt'],
                'end_dt': show['end_dt'],
                'long_day': show['start_dt'].strftime(LONG_DAY_FMT)
            } for show in shows]

            long_days = list({show['long_day'] for show in shows})
            long_days.sort(key= lambda x: datetime.strptime(x, LONG_DAY_FMT))

            self.shows = {long_day: [] for long_day in long_days}

            for show in shows:
                self.shows[show['long_day']].append(show)


        self.term_cols = get_terminal_size()[0]
        # self.max_lens = get_max_lens(self.shows) # lengths of show fields


def print_show(show, col_widths):
    """
    Given col_widths, print the show
    """

    pass


def get_col_widths(max_lens, term_size):
    """
    Return the col_widths to use
    Only title and subtitle to vary
    """

    pass



def split_line(line, max_width):
    """
    Return a list with the input line split to fit the max_width
    """

    # go through the line, stopping at last spaces before max_width


    out = [""]

    for word in line.split():
        print(word)

        # if the new word would overshoot, start a new line
        if len(word) + len(out[-1]) >= max_width:
            out.append(word)
        else:
            out[-1] = " ".join([out[-1], word])
        print('out after', out)

    out[0] = out[0].strip()

    return out



def compress_channel(channel_name):
    """
    Make a compressed version
    """

    channel_name = channel_name.replace('Sky Sports', 'Sky')
    channel_name = channel_name.replace('Eurosport', 'Eur')
    channel_name = channel_name.replace(' Event', '')

    return channel_name



def get_max_lens(shows):
    """
    Return the max length across each field in the passed shows
    """

    # set up empty dict for the variable fields
    maxes = {
        'title': 0,
        'subtitle': 0,
        'channel': 0,
        'c_channel': 0,
    }

    for field in maxes:
        longest = max(shows, key= lambda x: len(x[field]))
        maxes[field] = len(longest[field])

    return maxes


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
                    print(show['start_dt'].strftime("%a"), end=" ")

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


