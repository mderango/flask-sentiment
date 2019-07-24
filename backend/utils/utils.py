from datetime import datetime, timedelta

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_map = dict()
for i in range(1, 13):
    month_map[months[i]] = i

def convert_creation_timestamp(t):
    '''
    Converts created_at field to seconds since 1/1/1970 utc:
    Tue Jul 23 10:11:02 +0000 2019
    '''
    month = int(t[4:7])
    day = int(t[8:10])
    hour = int(t[11:13])
    minute = int(t[14:16])
    sec = int(t[17:19])
    year = int(t[-4:])

    ref = datetime(1970, 1, 1)

    return (datetime(year, month, day, hour, minute, sec) - ref).total_seconds()

def convert_integer_timestamp(t):
    '''
    Converts an integer timestamp to a string of a datetime object
    '''
    ref = datetime(1970, 1, 1)
    return ref + timedelta(seconds=t)
