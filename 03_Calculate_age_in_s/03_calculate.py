# -*- coding: UTF-8 -*-
"""
    Simple app calculates age in seconds.
"""

import datetime

def calculate_age(year, month, day):
    today = datetime.datetime.now()
    print today
    birth = datetime.datetime(year, month, day)
    print birth
    age = today - birth
    print age.total_seconds()

calculate_age(1987, 12, 29)
