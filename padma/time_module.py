import time
a = time.localtime()
print("print local time:",a)
cot = time.time()
print("print cot:",cot)
print(time.ctime(cot))
x = time.mktime(a)
print(x)



localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

a = time.time()
print(a)
b = time.localtime(a)
print(b)
c = time.asctime(b)
print(c)

n = time.asctime(b)
print(n)

z = time.strftime("%m/%d/%y")
print(z)

b = time.strftime("%y/%m/%d")
print(b)

#print(help(time.strftime))


cv = time.time()
print(cv)

nm = time.ctime(cv)
print(nm)

zx = time.sleep(1)
print("print cv:",cv)

from time import *
a = time()
print(a)
print(cv)
from time import time,ctime,asctime
a = time()
print(a)
print(cv)
print(ctime())
print(asctime())
from time import sleep
print(sleep(1))

