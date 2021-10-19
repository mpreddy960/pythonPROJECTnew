# #Python program to add two numbers
# #first type
# attend = 34
# attend1 = 46
# total = attend+attend1
# print(total)
# print("total elements firstelement {} second element {} total {}:".format(attend,attend1,total))
# delay = input("first number")
# delay1 = input(("second number"))
# total = float(delay)+float(delay1)
# print("print number1 {} number2 {} and total {} ".format(delay,delay1,total))
#
# decorate = 78
# decorate1 = 62
# depend =  decorate+decorate1
# print("print decorate {} ,decorate1 {} ,total {} ".format(decorate,decorate1,depend))
#
# borrow = input(["first number"])
# brush =input(["last number"])
# bulid = borrow+brush
# print("first number {} ,second number {} ,total {} ,".format(borrow,brush,bulid))

#Maximum of two numbers in Python

#first type
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
# Driver code
a = 2
b = 4
print(maximum(a, b))

def music(m,r):
    if m >= r:
        return m
    else:
        return r
m = 67
r = 45
print(maximum(m,r))

#second type


a = 2
b = 4

maximum = max(a, b)
print(maximum)

me = 343
he = 454
uesful = max(me,he)
print(uesful)

