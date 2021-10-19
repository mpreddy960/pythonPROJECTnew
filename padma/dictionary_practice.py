c = {23:34,45:98,"reddy":"malapati","malapati":"venkataravana"}
print(c)
b = c.values()
print(b)
x = c.keys()
print(x)
s = c.get("reddy")
print(s)
m = {2:4,45:67}
c.update(m)
print(c)
d = c.items()
print(d)
for x,y in d:
    print("print y:",y)
    print("print x :",x)

c.fromkeys("reddy")
print(c)
