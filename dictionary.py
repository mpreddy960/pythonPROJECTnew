a = {'sub':'chemistry','marks':'100','house':'duplex','percentage':'78%'}
print(a)
print(a.pop("percentage"))
print(a.keys())
print(a.values())
a.get('sub')
print(a)
print(type(a))
print(str(a))
print(list(a))
print(tuple(a))
print(a)
print(a.__len__())
print(a.items())
d = {'3':'torr','fox':'cunnig'}
print(d)
(a.update(d))
print(a)
s = (a.copy())
print(s)
print(s)
(s.clear())
print(s)
print(a.__dir__())
for call in a:
    print(call)
    for vote in call:
        print(call)

d = {1: "one", 2: "three"}
d1 = {2: "two"}
# updates the value of key 2
d.update(d1)
print(d)
d1 = {3: "three"}
# adds element with key 3
d.update(d1)
print(d)

print(d)
d["lock"] = 'koll'
d["goat"] = "bell"
print("new keys values :",d)

red = {"upper case":0,"lower case":1}
print(red)
t = {"you":45}
print(t)
red.update(t)
print(red)
