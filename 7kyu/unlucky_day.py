import calendar


def unlucky_day(year):
    count = 0
    for i in range(12):
        if calendar.weekday(year, i+1, 13) == 4:
            count += 1
    return count


"""
from datetime import date

def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))
"""


"""
from calendar import weekday

def unlucky_days(year):
    return sum(1 for i in xrange(1, 13) if weekday(year, i, 13) == 4)
"""


"""
from datetime import date

unlucky_days = lambda year: sum(date(year, month, 13).weekday() == 4 for month in range(1, 13))
"""
