#Python program to interchange first and last elements in a list

def vocabulary(consontration):
    length = len(consontration)
    print(consontration)
    trucaller = consontration[0]
    consontration[0] = consontration[length-1]
    consontration[length-1] = trucaller
    return consontration
conson = [12,34,45,56,67,78,89]
print(vocabulary(conson))

def common(ecart):
    world = len(ecart)
    door = ecart[0]
    ecart[0] = ecart[world-1]
    ecart[world-1] = door
    return ecart
episode = [67,54,34,54,56,65,67,78,78,7]
print(common(episode))

kept =[343,434,454,5565,454,343]
print("print original list :",kept)
kept.sort()
print("print sorted elements in a highest number:",kept[-1])

docs = [34,534,454,334,454,343]
print("print docs ;",docs)
print("print highest :",max(docs))


aim = [4543,434,3435,454,565,54,232,32]
print("print list :",aim)
aim.sort()
print("print smallest number in a list :",aim[0])

born = [545,4564,56756,454,5656,4545]
print("print born list :",born)
print("smalest number in a list :",min(born))

def confidencelevel(socity,socity1,socity2):
    socity[socity1],socity[socity2] = socity[socity2],socity[socity1]
    return socity
short = [34,343,3432,3432,34]
short1,short2 = 0,3
print(confidencelevel(short,short1,short2))

def household(hold,hold1,hold2):
    hold[hold1],hold[hold2] = hold[hold2],hold[hold1]
    return hold
hold = [545,4545,45345,4545,4354]
hold1,hold2 = 0,3
print(household(hold,hold1,hold2))

rain = [34,343,3434,3434]
print("before deleting list :",rain)
rain.clear()
print("after ddeleting list print :",rain)

hail = [232,6576,454,232,787]
strong = [898,767,656,454,45]
print("before deleting hail list :",hail)
print("before deleting strong list :",strong)
hail.clear()
strong.clear()
print("after deleting ematy list :",hail)
print("after deleting strong list print :",strong)

hailed = [767,565,545,4234,7]
print("before deleting list ;",hailed)
hailed *= 0
print("after deleting list print using *= 0 :",hailed)

chance = [5,6,4,3,2,9]
chance.reverse()
print("after revesing a list :",chance)


# Reversing a list using reverse()
def Reverse(lst):
    lst.reverse()
    return lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

confident = [1,2,3,4,5,6,7,8,9]
print(confident)
aim = confident[1:]
print(aim)
g = confident[::-1]
print(g)
b = confident[:-1]
print(b)
v = confident[7:]
print(v)
vc = confident[:-1]
print(vc)
botton = confident[1::]
print(botton)
xerox = confident[1:]
print(xerox)
print(confident.append("flower"))
print(confident)
confident.insert(2,'hotwater')
print(confident)

def got(pourstop):
     go = pourstop[::-1]
     return go
go = [1,2,3,4,5,6,7,8,9]
print("reversing a list :",got(go))

find = [1,2,3,4,5,6,7]
find.sort()
print("secon largest number in a list :",find[-2])

peacock = [-1,2,3,-4,5,-6,7]
for court in peacock:
    if court >= 0:
        print(court,end = ' ')

brown = [-1,-3,5,6,-9]
for topup in brown:
    if topup < 0:
        print(topup,end=' ')

highcourt = [1,2,3,4,5,6,7,8]
for u in range(1,5):
    print(u)
for problem in range(1,30):
    print(problem)

start,end = -6,10
for seriously in range(start,end):
    if seriously >= 0:
        print(seriously,end= " ")

# long = int(input("starting number"))
# ending = int(input("ending number"))
# for interger in range(long,ending):
#     if interger >= 0:
#         print(" print elements",interger,end= " ")

zone,fungal = -10,5
print(zone)
for target in range(zone,fungal):
    if target <= 0:
        print(target,end= " ")

# code = int(input("starting number"))
# barcode = int(input("ending number"))
# for go in range(code,barcode):
#     if go  <= 0:
#         print(go,end= " ")

felicition = [1,2,3,4,5,6,7]
print("print the list :",felicition)
consumer = 0
for yoyo in felicition:
    consumer = consumer+1
print("find the list length :",consumer,end= " ")

test_list = [1, 4, 5, 7, 8]
# Printing test_list
print("The list is : " + str(test_list))
# Finding length of list
# using loop
# Initializing counter
counter = 0
for i in test_list:
    # incrementing counter
    counter = counter + 1
# Printing length of list
print("Length of list using naive method is : " + str(counter))

vocabulary = []
vocabulary.append(23)
vocabulary.append(67)
vocabulary.append(45)
print(vocabulary)
print(len(vocabulary))

contract = [2,3,4,5,6,7,8,9]
print("print the list :",contract)
goaljob = len(contract)
print("print the liost length :",goaljob)

attractive = [1,2,3,4,5,6]
for guts in attractive:
     if(guts == 2):
         print("element in a list")

#
# est_list = [1, 6, 3, 5, 3, 4]
# print("Checking if 4 exists in list ( using loop ) : ")
# # Checking if 4 exists in list
# # using loop
# for i in test_list:
#     if (i == 4):
#         print("Element Exists")
#
# print("Checking if 4 exists in list ( using in ) : ")
# est_list = [1, 6, 3, 5, 3, 4]
#
# print("Checking if 4 exists in list ( using loop ) : ")
#
# Checking if 4 exists in list
# using loop
# test_list = [1,2,3,4,5,6]
# for i in test_list:
#     if (i == 4):
#         print("Element Exists")
#
# print("Checking if 4 exists in list ( using in ) : ")


seriouslygotthejob = [2,3,34,454,45]
if (34 in seriouslygotthejob):
    print("element in a list is correct")

if(43 in seriouslygotthejob):
    print("it is in a list ")
else:
    print("it is not availble")

for bird in seriouslygotthejob:
    if (bird == 46):
        print("element is exist")
    else:
        print("it is not availble")
