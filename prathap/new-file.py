mesir = [-2,-4,6,7,3,2,4,-5]
print(mesir)
for root in mesir:
    if root >= 0:
        print(root,end=',')

voltage = [1,2,3,4,56,7,8]
print("rint voltage :",voltage)
voltage.sort()
print("find second largest number in list :",voltage[-2])
def got(fort):
    result = 1
    for top in fort:
        result = result * top
    return result
folk =[2,3,4]
folk2 = [4,5,3]
print(got(folk))
print(got(folk2))

def holi(holi1,holi2,holi3):
    holi1[holi2],holi1[holi3] = holi1[holi3],holi1[holi2]
    return holi1
holi1 = [1,2,3,4]
holi2,holi3 = 1,3
print(holi(holi1,holi2,holi3))


fold = {"pysics":56,"maths":45,"koll":57}
print(fold)
fold["houses"] = 3
print(fold)
journy = [2,3,4,5,6,7]
print(journy)
journy.reverse()
print("reversing a list print :",journy)

toy,toll = -23,4
for volume in range(toy,toll):
    if volume >= 0:
        print(volume,end= ' ')
    else:
        "no data"

for niggard in range(-4,10):
    if niggard <= 0:
        print(niggard,end=" ")


sift = [2,3,4,5,6,6,7,65,5,7]
print(sift)
potentional = 0
for clarity in sift:
    potentional = potentional+1
print(potentional)

mutual = [1,2,3,4,5,6]
modern = len(mutual)
print(modern)

favourable = []
favourable.append(45)
favourable.append(2)
favourable.append(6)
favourable.append(9)
favourable.append(46)
print(favourable)
print(len(favourable))


spinkle = [3,4,5,6,7]
for spin in spinkle:
    if (spin == 4):
        print("element in a list ok ")

peeloff = [1,2,3]
for you in  peeloff:
    if (1 in peeloff):
        print("element exists in a list ")

times = [1,2,3,4,5,6,7,8,9]
count = times.count(7)
if count > 0:
    print("element 7 exists")

positivethinking = [1,2,3,43,5,6,7,8,9]
print(positivethinking)
positivethinking.clear()
print("clear list :",positivethinking)

add = [2,3,4,5]
story = [34,56]
add.insert(2,67)
print(add)
add.extend(story)
print(add)
got = ["reddy"]
add.extend(got)
print(add)
add.extend("malapati")
print(add)
# add.extend(67)
# print(add)
a = [123]
a.extend("dsd")
print(a)

reddy = [12,23,34,4]
for hi in reddy:
    print(hi)
    add.append(hi)
print(add)

add.append(story)
print(add)


def Nmaxelements(list1, N):
    final_list = []
    for i in range(0, N):
        print(i)
        max1 = 0
        for j in range(len(list1)):
            print("print j:",j)
            print("print list1 j:",list1[j])
            if list1[j] > max1:
                print("loopin max:",max1)
                max1 = list1[j];
                print("max1 print :",max1)

        list1.remove(max1);
        final_list.append(max1)
    print(final_list)
# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
# Calling the function
Nmaxelements(list1, N)

skinflint = [1,2,3,4,5,6,7,8,9]
print(skinflint)
n = 3
skinflint.sort()
print(skinflint[-n:])

