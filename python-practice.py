a = ('prathapreddy','python','job')
print(a)
print(type(a))
print(a.index("job"))
print(a.count('job'))
print(a)
s = 'once up on a time'
print(s)
print(type(s))
print(s.count('e'))
print(s.index("a"))
print(s.encode())
print(s.encode())
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace("time",'colum'))
print(s)
print(s.title())
print(s.find("e"))
print(s.isupper())
print(s.swapcase())
print(s)
print(s.swapcase())
print(s.join('job'))
print('python'.join(s))
print(s)
print(s.casefold())
#  Python program to add two numbers
a = 12
b = 38
print(a+b)#  sum
sum = a+b
print('sum of {},{},{}'.format(a,b,sum))
f = {'marks':"100",'telugu':'35','hindi':'45','maths':'70'}
print(f)
print(f.values())
print(f.keys())
print(f.get('maths'))
g = (f.copy())
print(g)
print(g)
print(g.items())
print(g.__len__())
print(g.pop('hindi'))
print(g)
print(f.popitem())
kiran = [32,44,34,232,42,23,22,4]
print(kiran)
print(type(kiran))
kiran.reverse()
print(kiran)
print(kiran.index(32))
kiran.sort()
print(kiran)
print(kiran.pop())
print(kiran)
kiran.extend('44')
print(kiran)
kiran.remove('4')
print(kiran)
kiran.append('klm')
print(kiran)
kiran.insert(2,'pople')
print(kiran)
kiran.remove('klm')
print(kiran)
kiran.clear()
print(kiran)
for prathapreddy in range(1,100):
    print(prathapreddy)

a = [2,3,4,5,2,2,2,3,4,5]
print(a)
print(set(a))
for j in a:
    print(j)
for h in range(1,45):
    print(h)
print(str(h))
print(type(h))
print(g)
print(type(g))
h = 'rgrthth'
print(h)
print(h.encode())
print(h)
print(h.isdecimal())
print(len(h))
for f in h:
    print(f)


# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
newlist = [8,4,89,567,8]
swapList(newlist)
print('jkl',newlist)



# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

[24, 35, 9, 56, 12]

