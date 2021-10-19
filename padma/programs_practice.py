
#Write a Python program to multiply all the items in a dictionary

se = {"tough":45,"route":15}
print(se)
got = 1
for i in se:
    got = got*se[i]
print("print got :",got)


def fo(g):
    t = 1
    for y in g:
        t = t*y
    return t
go = [1,2,3]
print("print all elements in a list :",fo(go))


#rite a Python program to sort a given dictionary by key

doleful = {"frog":"snake","dog":"cat","cat":"rat"}
for u in sorted(doleful):
    print(u)

#Write a Python program to check a dictionary is empty or not

buffet = {}
if buffet:
    print("empty dictionary ")
else:
    print("dictionary is not empty")

# count uppercae letters and lower case letters

def english(hindi):
    foe = 0
    toe = 0
    for malayalam in hindi:
        if malayalam.isupper():
            foe+=1
        elif malayalam.islower():
            toe+=1
        else:
            pass
    return foe,toe

english("PRATHAPreddy MALAPATI")

#maximum two numbers

def hight(a,b):
    if a >= b:
        return a
    else:
        return b

a = 3
b = 6
print(hight(a,b))
#maxium three numbers

def soak(a,b,c):
    if a>= b and a>=c:
        return a
    elif b>=c:
        return b
    else:
        return c
a = 8
b = 6
c = 10
print("print maxium number :",soak(a,b,c))

#inter change element position in a list

def future_tence(present_tence,past_tence,past_paticiple):
    present_tence[past_tence],present_tence[past_paticiple] = present_tence[past_paticiple],present_tence[past_tence]
    return present_tence
beforms = [1,2,3,4,"reddy","malapati"]
helping,verbs = 1,4
print("print interchage elements position:",future_tence(beforms,helping,verbs))

#change first and last element

def hi(ni):
    so = len(ni)
    rep = ni[0]
    ni[0] = ni[so-1]
    ni[so-1] = rep
    return ni
co = [1,2,3,4]
print(hi(co))


#multipaly all the elements in a dictionary

a= {"marks":23,"pysics":20}
v = 1
for f in a.values():
    print("print f:",f)
    v = v*f
print(v)
#practice another method
v = 1
for g in a:
    d = a[g]
    v = v*d
print(v)

#Write a Python program to get the 4th element and 4th element from last of a tuple

sang = (1,2,3,4,7,4,5,67,68,43,9)
print("print sang:",sang)
tup = sang[3]
print(tup)
tupl = sang[-4]
print("print 4th lost element i tuple :",tupl)

#Write a Python program to find the repeated items of a tuple

repeated = (1,2,3,4,5,54,54,54)
print("print repeated :",repeated)
y = repeated.count(54)
print("print repeated 54 :",y)

#Write a Python program to check whether an element exists within a tuple

fort = (1,2,3,4,45,"teddy")
print(fort)
if "teddy" in fort:
    print("it is exist")
else:
    print("not exist in a tuple")

#practice

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)

got = ("teddy","reddy","get",3,4,5,64)
print(got)
print(5 in got)
print(56 in got)

#Write a Python program to find the index of an item of a tuple

#bewilder = to confuse
bewilder = ("soldier","suffer","stop",2,3,4,3,2)
print(bewilder)
print(type(bewilder))
print(bewilder.index("soldier"))
print(bewilder.index("suffer"))

#Write a Python program to reverse a tuple

toy = (1,2,3,4,5)
print(toy)
joke = toy[::-1]
print("print reverse a tuple :",joke)

def go(went):
    vol = went[::-1]
    return vol
went = (1,2,3,4,5,6)
print("print reverse a tuple :",go(went))

#Write a Python program to replace last value of tuples in a list

list_of_tuples = [(1,2,3),(3,4),(5,6)]
box = []
for tuple in list_of_tuples:
    print("print tuple :",tuple[:-1])
    tup = tuple[:-1] + (10,)
    box.append(tup)
print("print box :",box)
#Write a Python program to read last n lines of a file.
n = 2
fo = open("a.txt")
go = fo.readlines()
jio = go[-n:]
print(jio)


#Write a Python program to count the number of lines in a text file.










pot = open("colum")
vo = pot.read()
no = vo.split("\n")
print("print split vo :",no)
co = 0
for i in no:
    if i :
        co += 1
    print(co)

#Write a Python script to check whether a given key already exists in a dictionar

g = {"one":34,"two":56}
print(g)
if "one" in g:
    print("element exist")
else:
    print("element not exist")

#Write a Python program to convert a tuple of string values to a tuple of integer values.

have = (("34","43"),("32","31"))
print(have)
print(type(have))

for h in have:
    print("print h:",h)
    joyful = int(h[0]),int(h[1])
    print("print joyful :",joyful)
    print("original strings:",have)

#Write a Python program to convert a given tuple of positive integers into an integer.

positive_numbers = (1,2,3,4,5)
print("positive elements :",positive_numbers)
for gel in positive_numbers:
    print(gel,end="")
print(type(gel))

#Write a Python function to insert a string in the middle of a string.

def middle(s1,s2):
    b = s1[:2] + s2 + s1[2:]
    return b
s1 = "rama"
s2 = "reddy"
print("print s1,s2:",middle(s1,s2))

#Write a Python function to create and print a list where the values are square
# of numbers between 1 and 30 (both included)

def df():
    ds = []
    for g in range(1,31):
        a = g**2
        ds.append(a)
    return ds
print(df())

#Write a Python function to create and print a list where the values are square
# of numbers between 1 and 30 (both included)

def v():
    l = []
    for b in range(1,31):
        c = b**2
        l.append(c)
    print(l)
print(v())



