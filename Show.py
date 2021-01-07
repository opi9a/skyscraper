# skyscraper/Show.py
"""
Helper class to hold info on a tv show
"""

import json
import pandas as pd

def get_show():
    # just a factory for a series with right index
    return pd.Series(index = [
            "title",
            "subtitle",
            "channel",
            "link",
            "start_time_raw",
            "start_dt",
            "end_dt",
            "duration",
        ]
    )

# class Show():
#     """
#     Class to hold show info
#     """
#     def __init__(self, show_dict=None):

#         if show_dict is not None:
#             self.__dict__ = show_dict

#         else:
#             self.title = None
#             self.subtitle = None
#             self.sports = None
#             self.sport = None
#             self.type = None
#             self.channel = 'unknown'
#             self.show_type = 'unknown'
#             self.link = None
#             self.live = False
#             self.date_raw = None
#             self.start_time_raw = None
#             self.end_time_raw = None
#             self.start_dt = None
#             self.end_dt = None
#             self.start_time = None # in isoformat strin
#             self.u_time = None
#             self.duration = None


#     def __setitem__(self, item, value):
#         self.__dict__[item] = value

#     def __getitem__(self, item):
#         return self.__dict__[item]


#     def __repr__(self):
#         return json.dumps(self.__dict__, indent=4, default=str)




