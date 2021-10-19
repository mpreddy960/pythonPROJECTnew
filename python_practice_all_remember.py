a = (2,3,4,5,6)
print(a)
print(type(a))
string = ("prathapreddy",34,434,45,12,76,87,67,76,76,34,45,"confidence","aim","tecnology","goal","sad","happy")
print(string)
print(type(string))
print(string.count(76))
print(string.count(45))
print(string.index("confidence"))
print(string.__len__())
print(str(string))
print(list(string))
print(set(string))
aim = ['level','looping','grooming','final','future','settle','such','brave']
print(aim)
print(type(aim))
print(aim.extend('goalconfidence'))
print(aim)
print(aim.sort())
print(aim)
print(aim.pop())
print(aim.pop(8))
print(aim.insert(2,'onceyouget'))
print(aim)
print(aim.append('journy'))
print(aim)
print(aim.reverse())
print(aim)
print(aim.__len__())
print(len(aim))
print(aim.__sizeof__())
print(aim.index('grooming'))
print(aim)
print(tuple(aim))
print(set(aim))
print(str(aim))
#print(int(aim))
print(aim)
solve = [9,5,0,5,3,5,7,9,6]
print(solve)
print(solve[2])
print(solve[5])
print(solve[3:-1])
print(solve[-2])
print(solve)
print(solve[-1])
print(solve[-6])
print(solve[7])
print(solve[-7])
print(solve[1:-1])
print(solve[3:-3])
print(solve[5:-2])
print(solve[8])
print(solve[-6])
print(solve[-3])
print(solve[-5:])
print(solve.sort())
print(solve)
print(solve.reverse())
print(solve)
print(solve.pop())
print(solve)
print(solve.insert(3,'aimgoals'))
print(solve)
print(solve.append("motivation"))
print(solve)
print(solve.count(9))
print(solve.index('motivation'))
print(solve.__sizeof__())
print(len(solve))

#Python program to interchange first and last elements in a list

#Swap
#function

def swapList(newList):
    size = len(newList)
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
# Driver code
newList = [12, 35, 9, 56, 24]
#print(swapList(newList))
a = swapList(newList)
print(a)
def reddy(prathap):
    size = len(prathap)
    temp =prathap[0]
    prathap[0] = prathap[size-1]
    prathap[size-1] = temp
    return prathap
prathap = [9,5,0,5,3,5,7,9,6,0]
print(reddy(prathap))

def joker(jell):
    long = len(jell)
    holi = jell[0]
    jell[0] = jell[long-1]
    jell[long-1] = holi
    return jell
jell = [565,565,56,56,565,454,34]

cofidencelevel = {"prathapreddy":"35","venkataravana":"67","feroj":"89","house":"62","45":"67"}
print(cofidencelevel)
print(type(cofidencelevel))
print(cofidencelevel.values())
print(len(cofidencelevel))
print(cofidencelevel.items())
print(cofidencelevel.__sizeof__())

#Python program to swap two elements in a list

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))

def changepositions(joker,joker1,joker2):
    joker[joker1],joker[joker2] = joker[joker2],joker[joker1]
    return joker
joker = [4,5,3,2,5,6]
joker1,joker2 = 1,2
print(changepositions(joker,joker1,joker2))

def aim(goal,goal1,goal2):
    goal[goal1],goal[goal2] = goal[goal2], goal[goal1]
    return goal
goal = [56,3,45,6,5765,454,54,45,56]
goal1,goal2 = 4,5
print(aim(goal,goal1,goal2))


def course(p1,p2,p3):
    p1[p2], p1[p3] = p1[p3], p1[p2]
    #p1[p3] = p1[p2]
    return p1
p1 = [9,5,0,5,3,5,7,9,6,0]
p2,p3 = 2,5
print(course(p1,p2,p3))

def gettingjob(part,part1,part2):
    part[part1],part[part2] = part[part2],part[part1]
    return part
part = [89,5,64,54,3,5]
part1,part2 = 2,5
print(gettingjob(part,part1,part2))

def guts(koll,koll1,koll2):
    koll[koll1],koll[koll2] = koll[koll2],koll[koll1]
    return koll
koll = [96,86,89,46,47]
koll1,koll2 = 0,4
print(guts(koll,koll1,koll2))



def house(goal,goal1,goal2):
    goal[goal1],goal[goal2] = goal[goal2],goal[goal1]
    return  goal
goal = ["goal","aim",9,3]
goal1,goal2 = 0,3
print(house(goal,goal1,goal2))


def aim(achive,achive1,achive2):
    achive[achive1],achive[achive2] = achive[achive2],achive[achive1]
    return achive
achive = ["hear","lived","prince","happy",]
achive1,achive2 = 1,2
print(aim(achive,achive1,achive2))

def attractive(look,look1,look2):
    look[look1],look[look2] = look[look2],look[look1]
    return look
look = ["broke","god","grey","bird","soul","dead"]
look1,look2 = 0,5
print(attractive(look,look1,look2))



#Python | Ways to find length of list
countble = ["uncountble","people","kill","colour",45,34,23,56,78,89]
print("the list :", (countble))
count = 0
for i in countble:
    count = count+1
print("find lenth :", (count))

actor = [34,3343,43,45,45,45,56,5,34,45,45,6]
print("print the list :",actor)
plural = 0
for crows in actor:

    plural = plural+1
print("find list length :",plural)

sumanth = [75,65,45,35,25,15]
print("disply  sumanth list :" ,sumanth)
decide = 0
for fell in sumanth:
    decide = decide+1
print(" sumanth length :",decide)


coachingperfect = [2,34,23,43,56,54,343]
print(coachingperfect)
print(coachingperfect[1:])
print(coachingperfect[3:])
print(coachingperfect[2:5])
print(coachingperfect[ :3])
print(coachingperfect)
print(coachingperfect.index(343))
print(coachingperfect.insert(4,"achivment"))
print(coachingperfect)
print(coachingperfect.append("correct"))
print(coachingperfect)
print(coachingperfect.reverse())
print(coachingperfect)
print(coachingperfect[:])
print(coachingperfect[-9:2])
print(coachingperfect[-9:5])
print(coachingperfect[-9:-2])
print(coachingperfect[-9:-5])

a = []
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The length of list is: ", len(a))

a = []
a.append("goal")
a.append("aim")
a.append("job goal")
a.append("concentration")
a.append("focused")
a.append("focus")
print("all of list length :" ,len(a))


focus = [23,43,32,43,45,34,232,"glow","mindful","music life","acting aim"]
print("print the list :", (focus))
fashion = 0
for g in focus:
    fashion = fashion+1
print("print list length :", (fashion))

sourya = [43,34,34,4,34,34,3,454,34,"highest","curry","housefull","mountain"]
print("print list :" ,(sourya))
voltage = 0
for hi in sourya:
    voltage = voltage+1
print("print list length :" ,(voltage))

boatique = [878,76,65,43,34,5,6,56,45,4,65,6,7,8,89,78,676,565,64,45]
print("print list total :" , (boatique))
guts = 0
for jai in boatique:
    guts = guts+1
print("lsit length :" , (guts))

mention = [45,54,34,4,76,78,"get well soon","better luck","get well","my pleasure","face to all",89,57,43,32]
print( "print total str int count :",mention)
really = 0
for say in mention:
    really = really+1
print("print counting list :",really)

a = []
a.append("aim")
a.append("coaching")
a.append("serious")
a.append("once u reach")
a.append("reach your goal")
print("total print :" , len(a))

aimjob = len([3,32,3,34,43,56,5,3,54,6,53,"goal python job","confirm job","concentration"])
print("list  total length :" , aimjob)

concentration = len(["you got job","he is fine","two days","thank you","bad luck","next time"])
print("print list length :",concentration)


#Check if element exists in list in Python
#first type
test_list = [1, 6, 3, 5, 3, 4]

print("Checking if 4 exists in list ( using loop ) : ")

# Checking if 4 exists in list
# using loop
for i in test_list:
    if (i == 4):
        print("Element Exists")

begin = [87,565,45,43,67,787,6,5,343,32,6,78,8]
print("checking 343 exists in list :")
for people in begin:
    if (people == 343):
        print("correct element")

rain = [45,43,423,43,23,2565,676,5,44,343,2,45,64,67]
print("check 676 :")
for buses in rain:
    if (buses == 676):
        print("it is element exists")

hgh = [454,64,54,34,334,45,454,565]
print("file 64 exists :")
for got in hgh:
    if (got == 64):
        print("ok list ")


#second type
reddy = [56,55,45,56,343,56]
print("Checking if 55 exists in list ( using in ) : ")
if (55 in reddy):
    print("Element Exists")






#Different ways to clear a list in Python
#first type
today = ["home town","next year","hero honda bike like","tomorrow","pieces",34,64,]
print("before clear list :",today)
today.clear()
print("after clear list :",today)
#second type
opportunity = ["he","she","it","them","they","will","must"]
opportunity1 = ["boat","people","aim","goal","ambition","serious goal"]
print("before clear list :",opportunity)
opportunity.clear()
print("after clear list :",opportunity)
print("before clear list1 :",opportunity1)
opportunity1.clear()
print("after clear list1 :",opportunity1)


a = "i am ramakrishnareddy "

print(a)
print(a.find("ramakrishna"))
print(a.index("ramakrishna"))
print(a.join("got"))
print(a.upper())
print(a.count("a"))
print(a[5:])
print(a.encode())
print(a.__len__())
print(type(a))
print(a.replace("reddy","padma"))

#Reversing a List in Python
#first type

def Reverse(lst):
    return [ele for ele in reversed(lst)]

# Driver Code
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

def recount(volume):
    return [ele for ele in reversed(volume)]

volume = [34,2,34,45,545,54,6,5,4,3,2,7,6,5,43]
print(recount(volume))

def failure(success):
    return [ele for ele in reversed(success)]

success = [1,2,3,4,5,6,7,8]
print(failure(success))

def planets(over):
    return [ele for ele in reversed(over)]
over = [778,57,343,565,98,898,464,454,56]
print(planets(over))

#second type

def Reverse(lst):
    lst.reverse()
    return lst

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

def replacereturn(killevery):
    killevery.reverse()
    return killevery

killevery = [9505357960,9604583987,7680853109,9686894647]
print(replacereturn(killevery))

def future(style):
    style.reverse()
    return style
style = [54,45,343,34,343,454,454,45,45,454,45,545,45,454,56,67]
print(future(style))



# Reversing a list using slicing technique
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10, 11, 12, 13, 14, 15,34,23,6,567,56,5,4,56,90]
print(Reverse(lst))

def decrease(old):
    system = old[::-1]
    return system
old = [354,45,53,343,454,565,454,34,45,54,454,45]
print(decrease(old))

def fungai(hold):
    going  = hold[::-1]
    return going
hold = [45,56,676,454,343,565,78,76]
print(fungai(hold))

def joker(bell):
    house = bell[::-1]
    return house
bell = [78.56,67,76.6,676.7,6576.6,67,676]
print(joker(bell))

#Python program to find sum of elements in list
#first type

total = 0
list1 = [11, 5, 17, 18, 23]
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)

acccept = 0
goal1 = [54,564,56,65,56,4645,56,76,5675,767]
for ele in range(0,len(goal1)):
    acccept = acccept + goal1[ele]
print("list total :",acccept)

asked = 0
arrange = [25,35,15,25]
for ele in range(0,len(arrange)):
    asked = asked + arrange[ele]
print("total list sum : ",asked)

#second type

list1 = [15,10,20,25, 15,25]
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
total = sumOfList(list1, len(list1))
print("Sum of all elements in given list: ", total)

#third type

list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list: ", total)

collect = [54,54,76,343,232,454,676,89]
print(sum(collect))

surya = [765,767,35,45,67,89]
journy  = sum(surya)
print(journy)

#Python | Multiply all numbers in the list

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
#driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

def multiplyalllist(newlist):
    folk = 1
    for holi in newlist:
        folk = folk * holi
    return folk
goal1 = [34,2,23,34]
goal2 = [545,534,343,455]
print(multiplyalllist(goal1))
print(multiplyalllist(goal2))

def numeric(dellite):
    member = 1
    for high in dellite:
        member = member * high
    return member
ucg = [2,3,4]
ucg1 = [5,6,2]
print(numeric(ucg))
print(numeric(ucg1))

#Python program to find smallest number in a list

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:", *list1[:1])

hightest = [45,545,654,645,765,78,89]
hightest.sort()
print("find a smallest numbeer :",hightest[:1])

join = [85,6745,65,454,3345,6767]
join.sort()
print("list smallest number :",join[:1])

koin = [8,89,6,7,5,6,344,556,67]
koin.sort()
print("small number in a list :",koin[:1])

# Python program to find smallest
#second type
list1 = [10, 20, 1, 45, 99]
print("Smallest element is:", min(list1))

doing = [676,56,657,56,65,56,55]
print("small number :",min(doing))

bottle = [56,56,56,45,4465,67,565,567]
print("small number :",min(bottle))

# Python program to find smallest
# number in a list

#l = [int(l) for l in input("List:").split(",")]
#print("The list is ", l)
port = []
soul = "2,3,45,6,7"
soul1 = soul.split(",")
for l in soul1:
    port.append(int(l))
print(port)


# Assign first element as a minimum.
min1 = l[0]

for i in range(len(l)):

    # If the other element is min than first element
    if l[i] < min1:
        min1 = l[i]  # It will change

print("The smallest element in the list is ", min1)


# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

# print maximum element
print("Smallest element is:", min(list1))


