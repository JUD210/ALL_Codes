# https://www.hackerrank.com/challenges/python-time-delta/problem


import datetime

# datetime.strptime(date_string, format)
# is equivalent to
# datetime(*(time.strptime(date_string, format)[0:6]))
# except when the format includes sub-second components or timezone offset information, which are supported in datetime.strptime but are discarded by time.strptime.

"""
x = datetime.datetime.now()
print(x)
# 2019-01-11 12:14:34.872986

x = datetime.datetime(2019, 1, 11)
print(x.year)
# 2019
print(x.strftime("%a %d %b %Y %H:%M:%S %z"))
# Fri 11 Jan 2019 00:00:00

# A reference of all the legal format codes
# https://www.w3schools.com/python/python_datetime.asp

"""


""" Solution """
fmt = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())):
    # 2

    t1 = datetime.datetime.strptime(input(), fmt)
    t2 = datetime.datetime.strptime(input(), fmt)
    print(int(abs((t1 - t2).total_seconds())))

    # Sun 10 May 2015 13:54:36 -0700
    # Sun 10 May 2015 13:54:36 -0000
    # 25200

    # Sat 02 May 2015 19:54:36 +0530
    # Fri 01 May 2015 13:54:36 -0000
    # 88200
