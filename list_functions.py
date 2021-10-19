#  Python program to print positive numbers in a list

fig = [6,5,5,4,3,-7,-8,-9,4]
print(fig)
f  = []
def get_ele(fig):
    """teddyjjjj"""
    for ty in fig:
        if ty >=0:
            f.append(ty)
            print(ty, end=',')
    return f
# first to last element

g = get_ele(fig)
print(get_ele.__doc__)
print(g)
f = [2,4,3,2,4,2,3,4]
print(f)
k = f[::-1]
print(k)

#  Python program to print all positive numbers in a range

start,end = -2,20
for doll in range(start,end):
    if doll >= 0:
        print(doll,end=',')


#  Python program to print all negative numbers in a range

python,pythonjob = -10,28
for jobsettle in range(python,pythonjob):
    if jobsettle <  0:
        print(jobsettle,end=',')
#  Remove multiple elements from a list in Python

# list1 = [11, 5, 17, 18, 23, 50]
#
# for ele in list1:
#     if ele % 2 == 0:
#         list1.remove(ele)

# print("New list after removing all even numbers: ", list1)
# Output:

#  Python – Remove empty List from List

testlist = [1,2,3,[],[],5,6,7]
print(testlist)
