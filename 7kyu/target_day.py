import math
import datetime


def date_nb_days(a0, a, p):
    start = datetime.datetime.strptime('2016-01-01', '%Y-%m-%d')
    n_day = 1+int(math.log(a/a0,1+p/36000))
    end = start+datetime.timedelta(n_day)
    return end.strftime('%Y-%m-%d')


"""
from math import log, ceil
from datetime import date, timedelta as td

def date_nb_days(a0, a, p):
    n = log(a, 1 + p/36000.0) - log(a0, 1 + p/36000.0)
    return str(date(2016, 1, 1) + td(ceil(n)))
"""


"""
import datetime as dt
from math import log

def date_nb_days(a0, a, p, d=0):
  return str(dt.date(2016,1,1)+dt.timedelta(log(a/a0)/log(1+p/36000)+1))
"""
