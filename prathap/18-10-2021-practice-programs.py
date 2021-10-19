#odd numbers in list
reddy = [1,2,3,4,5,6,7,8,454]
for topranker in reddy:
    if topranker % 2 ==0:
        print("even numbers:",topranker,end=" ,")
#prime numbers
start = 30
ending = 56
for i in range(start,ending+1):
    print("print i ::::;:",i)
    if i>1:
        #print("print i:::::",i)
        for j in range(2,i):
            print("print j:::",j)
            if (i % j==0):
                break
        else:
                print("print prime numbers :::",i)

start = 11
end = 25
for i in range(start, end+1):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            print(i)

num = 64

if num > 1:
    for h in range(2,int(num/2)+1):
        if (num % h) ==0:
            print("it is not a prime number",num)
        else:
            print("it is a prime number")
else:
    print("it is not prime number")

number= 67

if number > 1:
    for klm in range(2,int(number/2)+1):
        if (number % klm) ==0:
            print("it is not a prime number",number)
        else:
            print("it is a prime number",number)
else:
    print("it is not prime number")

## Function for nth Fibonacci number

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
# First Fibonacci number is 0
    elif n == 1:
        return 0
# Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        print("n value:::",n)
        #print("Fibonacci(n-1)", Fibonacci(n-1))
        #print("Fibonacci(n-2)", Fibonacci(n-2))
        print("Fibonacci(n-1)+Fibonacci(n-2)", Fibonacci(n-1)+Fibonacci(n-2))
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(10))

#add two numbers
reddy = 23
hold = 67
cv = reddy+hold
print("add two numbers :",cv)
print("number of {0} and {1} total {2}".format(reddy,hold,cv))

#Wfactorial number in python

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         n*factorial(n-1)
# n = 5
# print(factorial(n))

import math

def reddy(n):
    return (math.factorial(n))
vol = 5
print(reddy(vol))

#Python Program to find sum of array

# Python 3 code to find sum
# of elements in given array
def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)
arr = []
arr = [12, 3, 4, 15]
n = len(arr)
ans = _sum(arr)
print('Sum of the array is ', ans)

#second method
arr = [12, 3, 4, 15]
ans = sum(arr)
print ('Sum of the array is ',ans)

#find second largest number in a list
list1 = [10, 20, 4, 45, 99, 2, 35, 45, 99, 78, 99]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))

music = [18,89,15,42,12]
listen = set(music)
print(listen)
listen.remove(max(listen))
print(max(listen))

#find all positive numbers in list

list_postive_numbers = [-1,-2,-3,-4,-5,-6,1,2,3,4,5,6,7,8]
for list in list_postive_numbers:
    if list >= 0:
        print("print positive numbers ",list)

#find all nagative numbers in a list,or tuplelist_postive_numbers
nagative = [1,-10,-2,3,-4,5,-6,7,-8]
for lis in nagative:
    if lis < 0:
        print("print nagative numbers :",lis)
folder = (-1,-1,-1,9,7,5,3,-35,)
print(folder)
for i in folder:
    if i<0:
        print("print nagative numbers",i)

#remove ematy list

test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []]
print ("List after empty list removal : " + str(res))


ematy_list = [2,3,[],4,[],5]
print("before list:",ematy_list)
for ele in ematy_list:
    list = []
    if ele != []:
        print(ele)
    else:
        pass



#
# test_list = [5, 6, [], 3, [], [], 9]
# print("The original list is : " + str(test_list))
# res = list(filter(None, test_list))
# print ("List after empty list removal : " + str(res))

#REMOVE EMATY TUPLES IN A LIST

def tuples(tuple):
    truple = filter(None,tuple)
    return truple
ematy_tuple = [2,3,4,(),(),(2,4)]
print(tuples(ematy_tuple))


def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

#check it is palindrome or not

reddy = "lolol"
print(reddy)
gh = reddy[::-1]
if reddy == gh:
    print("it is palindrome")
else:
    print("it is not palindrome")

palidrome_list = "malayalam"
job = ""
for i in palidrome_list:
    record = i+job
    if palidrome_list ==record:
        print("it is a palindrome string")
    else:
        "print it is a palindrome string"

#Reverse words in a given String in Python

def string(hour):
    got = hour.split()
    fgo = " ".join(reversed(got))
    return fgo
foalder = "my name is prathapreddy"
print(string(foalder))

#Reverse words in a given String in Python

def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
input = "geeks quiz practice code"
print (rev_sentence(input))

#Python program to check whether the string is Symmetrical or Palindrome

def palindrome(a):
    mid = (len(a) - 1) // 2  # you can remove the -1 or you add <= sign in line 21
    start = 0  # so that you can compare the middle elements also.
    last = len(a) - 1
    flag = 0
    while (start <= mid):

        # comparing letters from right
        # from the letters from left
        if (a[start] == a[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break;
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
def symmetry(a):
    n = len(a)
    flag = 0
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2
    start1 = 0
    start2 = mid
    while (start1 < mid and start2 < n):
        if (a[start1] == a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
string = 'amaama'
palindrome(string)
symmetry(string)

#tuple packing and unpacking
#Packing and Unpacking
#In packing, we place value into a new tuple while in unpacking we extract those values back into variables.

x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)