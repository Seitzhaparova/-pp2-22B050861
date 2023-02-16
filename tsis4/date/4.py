#Write a Python program to calculate two date difference in seconds.
from datetime import datetime, time


def func(d1, d2):
    x=d2-d1
    x_sec=x.days*24*3600 + x.seconds
    return x_sec
date1=datetime(2004, 8, 8)
date2=datetime.now()
ans=func(date1, date2)
print("I'm alive for " + str(ans) + ' seconds')

