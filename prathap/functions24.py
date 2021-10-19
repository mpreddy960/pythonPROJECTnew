# Given a list, write a Python program to swap first and last element of the list.
#
# Examples:

def newlist(fell):
    size = len(fell)
    temp = fell[0]
    fell[0] = fell[size-1]
    fell[size-1] = temp
klm = [4,5,6,7,8]
newlist(klm)
print(klm)

def newlist(fell):
    size = len(fell)
    temp = fell[0]
    fell[0] = fell[size-1]
    fell[size-1] = temp
klm = [4,5,6,7,8]
newlist(klm)
print(klm)


#  Python program to swap two elements in a list

def listhigh(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [8,3,9,45,4]
pos1 = 2
pos2 = 4
print (listhigh(list,pos1,pos2))

#  Python | Ways to find length of list

# # Initializing list
# test_list = [ 1, 4, 5, 7, 8 ]
#
# # Printing test_list
# print ("The list is : " + str(test_list))
#
# # Finding length of list
# # using loop
# # Initializing counter
# counter = 0
# for i in test_list:
#
#     # incrementing counter
#     counter = counter + 1
#
# # Printing length of list
# print ("Length of list using naive method is : " + str(counter))
# Output :
#
# The list is : [1, 4, 5, 7, 8]
# Length of list using naive method is : 5

# of len()
n = len([10, 20, 30])
print("The length of list is: ", n)
g = len(['fgf','fgfg','fgfg',4,3,3,454,34,565,343,676,454,343,242,565])
print(g)

# Different ways to clear a list in Python

list1 = [4,4,5,6,6,7]
list2 = [5,9,7,5,1,8,76]
print ("List1 before deleting is : ", list1)

list1.clear()
print(list1)
print("List1 after clearing using clear() : "+ str(list1))
print("List2 before deleting is : "+ str(list2))
list2.clear()
print(list2)
print("List1 after clearing using clear() : "+ str(list2))
list2 = []
print(list2)

d = [45,6,6,6]
print(d)
def ty(dff):
    print(dff)
    dff.clear()

ty(dff=d)
print(d)


# Reversing a List in Python

def ink(pop):
    return [ele for ele in reversed(pop)]
pop = [2,8,6,5,4,3,2]

print(reversed(pop))
print(pop)
print(reversed(pop))

# Python program to find sum of elements in list

total = 0
# creating a list
list1 = [11, 5, 17, 18, 23]
# Iterate each element in list
# and add them in variale total
for ele in range(0, len(list1)):
    #print(list1)
    total = total + list1[ele]
    #print(ele)
# printing total value
print("Sum of all elements in given list: ", total)
south = 0
poppy = [454,657,55,343,545,3434,3535]
for b in range(0,len(poppy)):
    south = south+poppy[b]
print('total sum:',south)
print(sum(poppy))

#  Python | Multiply all numbers in the list

def multiply(one):
    houses = 1
    for h in one:
        houses = houses*h
    return houses
two = [4,5]
three = [5,5]
print(multiply(two))
print(multiply(three))
print(sum(two))

#  Python program to find smallest number in a list

but = [32,343,2,42224]
print(but)
(but.sort())
print(but)
print('small number:',but[:1])


bu = [32,343,256,42224]
print(bu)
print('small number:',min(bu))

#  Python program to find largest number in a list

data = [656,5656,4646,3,343,454]
print(data)
(data.sort())
print(data)
print('high number :',data[-1])
print('high number :',max(data))

#  Python program to find second largest number in a list

a = [656,56,6546,565,44,46,6546,5,]

#  Python program to print even numbers in a list

f = [43,343,43,23,3,35,34,35,34,98,6,66,44,80]
print(f)
for num in f:
    if num % 2 == 0:
       print(num, end = ',')

#  Python program to print odd numbers in a List

hope = [54,76,7,9,3,1,19]
print(hope)
for jh in hope:
    if jh % 2 != 0:
        print(jh, end = ',')
start,end = 2,8
for fort in range(start,end):
    if fort % 2 == 0:
        print(fort,end = ',')

tyr,gh = 2,16
for gel in range(tyr,gh):
    if gel % 2 ==0:
        print(gel)

#  Python program to print negative numbers in a list

pythonjob = [-3,-4,-5,-6,-6,7,8,-2,-8,9,6,4]
print(pythonjob)
for hot in pythonjob:
    if hot < 0 :
       print(pythonjob,end='')

#

# Python program to print negative Numbers in a List

# list of numbers
list1 = [-10, 21, -4, -45, -66, 93]
num = 0

# using while loop
#Awhile (num < len(list1)):

    # checking condition
  #  if list1[num] < 0:
   #     print(list1[num], end=" ")

    # increment num
    #num += 1
g = [4,6,3,-4,-5,-8]
j = 0
while (j<len(g)):
    if g[j]<0:
        print(g[j],end=',')