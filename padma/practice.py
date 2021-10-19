#Write a Python script to check whether a given key already exists in a dictionar

g = {"one":34,"two":56}
print(g)
if "one" in g:
    print("element exist")
else:
    print("element not exist")

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




d= {"fe":45,"do":34}
for t in d:
    print(t)