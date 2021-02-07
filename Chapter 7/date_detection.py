#!/usr/bin/env python3
# date_detection.py - it detects whether a date is correct

import re


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(day, month, year):
    # february - 28 days & 29 days on leap years
    if month == 2:
        if day > 29:
            print('February doesnt have more than 29 days.')
            return False
        elif day == 29 and not is_leap_year(year):
            print('February only got 29 days on leap years and this is not a leap year.')
            return False
    # april, june, september, november - 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            print('These month have only 30 days')
            return False
    # rest of months - 31 days
    else:
        if day > 31:
            print('These month have only 31 days')
            return False
    print('Valid date!')
    return True


def is_date(date):
    regex = re.compile(r'(\d\d)/(\d\d)/(\d{4})')
    mo = regex.search(date)
    if mo is not None:
        day, month, year = mo.groups()
        return is_valid_date(int(day), int(month), int(year))
    else:
        print('Invalid date')
        return False


date = "31/09/2000"
is_date(date)
