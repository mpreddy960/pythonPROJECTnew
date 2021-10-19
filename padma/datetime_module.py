#datetime
import datetime
v = datetime.datetime(2021,7,13,4,31,45,454)
print(v)

n = datetime.datetime.now()
print(n)

c = datetime.datetime.today()
print(c)



print("print year :",c.year)
print("print month:",c.month)
print("print date:",c.date())
print("print hour:",c.hour)
print("print minute:",c.minute)
print("print sec:",c.second)
print("print milli second :",c.microsecond)
print("print day:",c.day)
print("print days:",c.weekday())
