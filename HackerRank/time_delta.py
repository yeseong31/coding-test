import datetime


def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.datetime.strptime(t1, format_string)
    t2 = datetime.datetime.strptime(t2, format_string)
    diff = t1 - t2
    return str(int(abs(diff.total_seconds())))


print(time_delta(
    'Sat 02 May 2015 19:54:36 +0530',
    'Fri 01 May 2015 13:54:36 -0000'))
