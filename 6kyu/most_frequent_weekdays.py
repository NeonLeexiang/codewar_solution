import datetime


weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year):
    year = str(year) if year > 999 else (4-len(str(year)))*'0' + str(year)
    start_year = year+'-1-1'
    end_year = year+'-12-31'
    starts = datetime.datetime.strptime(start_year, '%Y-%m-%d').weekday()
    ends = datetime.datetime.strptime(end_year, '%Y-%m-%d').weekday()
    return weekdays[starts:ends+1] if starts < ends else weekdays[0:ends+1]+weekdays[starts:7]

