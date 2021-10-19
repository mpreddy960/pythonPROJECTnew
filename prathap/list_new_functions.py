a = [2,34,55,1,2,3,4,5,6,7,8,8,9,8,6,5]
print(a)
print(a.index(2))
print(a.count(8))
print(a.pop())
print(a)
a.sort()
print(a)
a.insert(1,123)
print(a)
a.append(67)
print(a)
a.remove(34)
print(a)
a.reverse()
print(a)
a.extend('343')
print(a)
print(a.__len__())
print(len(a))
print(a)
print(type(a))
print(str(a))
print(tuple(a))
print(set(a))
g = a.copy()
print(g)
print(len(g))
print((a))
print(a[1])
print(a[1:5])
print(a[5:])
print(a[:-9])
print(a[2:-9])
print(a)
print(a[-2:])
print(a[:1])
print(a[:-9])

#swap interchange list in a two elements
def serious(horliks,horliks1,horliks2):
    horliks[horliks1],horliks[horliks2] = horliks[horliks2],horliks[horliks1]
    return horliks
horliks = [343,34,65,76,787,54,3,54]
horliks1,horliks2 = 0,4
print(serious(horliks,horliks1,horliks2))



voltage = [34,45,56,67,78,89,23]
print(len(voltage))
voltage.insert(4,voltage[0])
voltage.pop(0)
#voltage[4] = voltage[0]
print(voltage)


numeric = []
numeric.append(2)
numeric.append(4)
numeric.append(7)
print(numeric)
print(len(numeric))

def going(listsign):
    length = len(listsign)
    fold = listsign[0]
    listsign[0] = listsign[length-1]
    listsign[length-1] =  



