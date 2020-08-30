mouth = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06',
         "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}


def driver(data):
    # Start driving here!
    output = list()
    output.append(str.upper(data[2] if len(data[2]) <= 5 else str.upper(data[2][:5])))
    output.append("9"*(5-len(data[2])))
    output.append(data[3][-2])
    output.append(mouth[data[3][3:6]] if data[4] == "M" else str(int(mouth[data[3][3:6]])+50))
    output.append(data[3][0:2])
    output.append(data[3][-1])
    output.append(data[0][0])
    output.append(data[1][0] if data [1] != "" else "9")
    output.append("9AA")
    return ''.join(output)


"""
from datetime import datetime


def driver(data):
    first, middle, last, dob, gender = data
    try:
        d = datetime.strptime(dob, '%d-%b-%Y')
    except ValueError:
        d = datetime.strptime(dob, '%d-%B-%Y')

    return '{:9<5}{[2]}{:0>2}{:0>2}{[3]}{[0]}{[0]}9AA'.format(
        last[:5].upper(),
        str(d.year),
        d.month + (50 if gender == 'F' else 0),
        d.day,
        str(d.year),
        first,
        middle if middle else '9')
"""


"""
months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

def driver(data):
    first, middle, surname, birth, sex = data
    day, month, year = birth.split("-")
    
    return "%s%s%02d%s%s%s%s9AA" % ((surname.upper() + "9999")[:5],
            year[-2], months.index(month[:3]) + (51 if sex == "F" else 1),
            day, year[-1], first[0], (middle + "9")[0])
"""





