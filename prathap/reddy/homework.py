reddy ="WATER"
print(reddy)
reddy.upper()
print(reddy)
reddy.lower()
print(reddy)

#Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1  #d["uppercase"]+1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
            pass

    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test('The quick Brown Fox')



def doleful(glance):
    miserable={"reckon":0,"shove":0}
    for got in glance:
        if got.islower():
            miserable["shove"] = miserable["shove"]+1
        if got.isupper():
            miserable["reckon"] = miserable["reckon"]+1
        else:
            pass
    print("print upper case characters",miserable["reckon"])
    print("print lower case charaters",miserable["shove"])
    print("original string",glance)
doleful("Iam prathap REDDY")



#Write a Python program to reverse a string.

def reverse(string):
    reverse_string = ""
    for rever in string:
        #print("print rever :",rever)
        reverse_string = rever+reverse_string
        #print("reverse string :",reverse_string)
    print(reverse_string)
revers = "prathapredddy"
print("print revers function :",revers)
reverse(revers)

#practice

def run(string):
    reverse_string = ""
    for hi in string:
        reverse_string = hi+reverse_string
    print(reverse_string)
reddy = "prathapreddy"
print("print reddy :",reddy)
run(reddy)

#Write a Python function to multiply all the numbers in a list

def multiply(mylist):
    real = 1
    for list in mylist:
        real = real*list
    return real
list1,list2  = [1,2,3],[2,3,4]
print(multiply(list1))



#Write a Python function that takes a list and returns
# a new list with unique elements of the first list

listhigh = [1,2,3,2,4,4,23,3,43,23,23,43]
unique_element = []
for element in listhigh:
    if element not in unique_element:
        unique_element.append(element)
print("print unique element :",unique_element)
print("print set vunique elements:",list(set(listhigh)))

#Python program to check if a string is palindrome or not

def isPalindrome(s):
    return s == s[::-1]
# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")



def f(h):
    foe = 0
    goe = 0
    for g in h:
        if g.isupper():
            foe = foe+1
        elif g.islower():
            goe = goe+1
        else:
            pass

    return foe,goe
g = "PRAthap reddy"
print(f(g))

revevesed_list = [1,2,3,5,7]
print(revevesed_list)
doc = revevesed_list[::-1]
print(doc)

#Write a Python function to create and print a list
# where the values are square of numbers between 1 and 30 (both included)

sqr_list = []
for i in range(1, 31):
    #print("print i :",i)
    sqr_list.append(i * i)
    print("print sque list:",sqr_list,end=" ")


def upper_case(lower_case):
    g = {"toy":0,"goy":0}
    for to in lower_case:
        if to.isupper():
            g["toy"]+=1
        elif to.islower():
            g["goy"]+=1
        pass
    print("original string :",lower_case)
    print("print uppercase letters:",g["toy"])
    print("print lower case letters :",g["goy"])
upper_case("prathap REDDY")


#Write a Python script to add a key to a dictionary

dictionary = {23:45,56:78,"reddy":"malapati"}
print(dictionary)
dictionary.update({34:67})
print("print update a dictionary :",dictionary)


##Write a Python function to create and print a list
# where the values are square of numbers between 1 and 30 (both included)

for t in range(1,31):
    list = []
    list.append(t*t)
    print(list,end=" ")
#Write a Python script to check whether a given key already exists in a dictionary
g = {34:45,45:67}
for t in g:
    if {34:45} in t:
        print("file exist")
    else:
         print("file not exist")

dict = {"23":"34","12":"35"}
for t in dict:
    print(t)

# exist = {"marks":45,"persentage":78}
# if "makrs" in exist:
#     print("print file exist in dictionary")
# else:
#     "not exist in a dictionary"


#Write a Python program to sort a given dictionary by key



diction= {}
diction[34] = 45
diction[56] = 56
print(diction)
for t in sorted(diction.keys()):
    print(t,end=",")

#Write a Python program to multiply all the items in a dictionary

vol = {"folks":20,"goals":3}
replase = 1
for t in vol:
    replase = replase*vol[t]
print("print multiply all numbers:",replase,end=" ")

#Write a Python program to check a dictionary is empty or not


d= {}
if not bool(d):
    print("print ematy dictionary")


throw = {"presentence":"easy","past tence":"midium"}
beforms = {}
if throw:
    print("print throw is not ematy")
else:
    "print ematy"
if beforms:
    print("print beforms ematy dictionary")
else:
    print("print not ematy")


