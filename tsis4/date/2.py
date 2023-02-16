#Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
tod=datetime.now()
yes=tod-timedelta(days=1)
tom=tod+timedelta(days=1)
print("today is: "+ tod.strftime("%x"))
print("yesterday was: "+ yes.strftime("%x"))
print("tomorrow will be: "+ tom.strftime("%x"))

#print("esterday, today, tomorrow")