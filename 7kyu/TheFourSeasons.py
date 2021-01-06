"""
    date:       2021/1/6 11:56 下午
    written by: neonleexiang
"""
from datetime import datetime

spring_start, spring_end = datetime.strptime('03-21', '%m-%d'), datetime.strptime('06-20', '%m-%d')
summer_start, summer_end = datetime.strptime('06-21', '%m-%d'), datetime.strptime('09-20', '%m-%d')
autumn_start, autumn_end = datetime.strptime('09-21', '%m-%d'), datetime.strptime('12-20', '%m-%d')
winter_start, winter_end = datetime.strptime('12-21', '%m-%d'), datetime.strptime('03-20', '%m-%d')

year_start = datetime.strptime('01-01', '%m-%d')


def four_seasons(d):
    if d > 365:
        return 'The year flew by!'
    elif d < (winter_end - year_start).days:
        return 'Winter Season'
    elif d < (spring_end - year_start).days:
        return 'Spring Season'
    elif d < (summer_end - year_start).days - 1:
        return 'Summer Season'
    elif d < (autumn_end - year_start).days + 1:
        return 'Autumn Season'
    else:
        return 'Winter Season'

