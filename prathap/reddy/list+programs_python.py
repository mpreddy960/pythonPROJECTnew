#Python program to interchange first and last elements in a list
#first type
def swapList(newList):
    size = len(newList)
    print(newList)
    temp = newList[0]
    print("temp element :",temp)
    newList[0] = newList[size - 1]
    print("holi", newList)
    newList[size - 1] = temp
    print("change elements :",newList)
    return newList

newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#second type

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList
newList = [23, 56, 9, 56, 98]
print(swapList(newList))

#third type

def swapList(list):
    get = list[-1], list[0]
    list[0], list[-1] = get
    return list
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#Python program to swap two elements in a list


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))

def swappositions(postion1,postion2,postion3):
    postion1[postion2],postion1[postion3] = postion1[postion3],postion1[postion2]
    return postion1
postion1 = [4,434,454,565,676,565]
postion2,postion3 = 1,3
print(swappositions(postion1,postion2,postion3))


def swapPositions(box, pos1, pos2):
    # popping both the elements from list
    first_ele = box.pop(pos1)
    print(first_ele)
    print("after poping elements ",box)
    second_ele = box.pop(pos2 - 1)
    print("second pop :",box)
    # inserting in each others positions
    box.insert(pos1, second_ele)
    box.insert(pos2, first_ele)
    return box
box = [23, 65, 19, 90]
pos1 = 0
pos2 = 2

print(swapPositions(box,pos1 ,pos2))

#Python | Ways to find length of list
#first type

test_list = [1, 4, 5, 7, 8]
counter = 0
for i in test_list:
    # incrementing counter
    print("counter print :",counter)
    counter = counter + 1
    print("couter list :",counter)
# Printing length of list
print("Length of list using naive method is : ",(counter))

#practice

fine = [545,545,454,545,54]
house = 0
for folk in fine:
    house = house + 1
print("lenth list : ",house)

#second type

a = ["swap","math"]
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The length of list is: ", len(a))
#practice
dove = []
dove.append(343)
dove.append("help")
dove.append("prathap")
dove.append("padma")
dove.append("ramakrishna")
print("list length :",len(dove))

listlength = []
listlength.append(33)
listlength.append(67)
listlength.append(87)
print("total list length :",len(listlength))

#Check if element exists in list in Python

#first type

# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

print("Checking if 4 exists in list ( using loop ) : ")

# Checking if 4 exists in list
# using loop
for i in test_list:
    if (i == 4):
        print("Element Exists")
#pratice

focus = [23,334,54,56,67,56,65]
for guts in focus:
    if (guts == 56 ):
        print("yes exists in a list 56 :")

#second type

print("Checking if 4 exists in list ( using in ) : ")

# Checking if 4 exists in list
# using in
if (4 in test_list):
    print("Element Exists")



prathapreddy = [2,3,3,5,6,7,67,78]
if (67 in prathapreddy):
    print("checking is correct :")

#third type

test_list = [10, 15, 20, 7, 46, 2808]

print("Checking if 15 exists in list")

# number of times element exists in list
exist_count = test_list.count(15)
print(exist_count)

# checking if it is more then 0
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

#practice

padmareddy = [5,45,343,5656,656,56565]
ramakrishnareddy = padmareddy.count(45)
if ramakrishnareddy > 0:
    print("yes , 45 exists in a list ")
else:
    print("no , 45 doesn't exists : ")

if ramakrishnareddy >1:
    print("yes ")
else:
    print("no")


