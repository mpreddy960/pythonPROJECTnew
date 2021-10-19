honest = [45,45,565,56,565655,6565,56,75]
honest.sort()
print("hightest number in list :", honest[-1])

quatar = [67,56,556,54654,67,6867]
quatar.sort()
print("largest :",quatar[-1])

goal = [435,454,343,45,5,4,45]
goal.sort()
print("smallest number in list :",goal[0])


#inter change list in a elements
def mother(mom,mom1,mom2):
    mom[mom1],mom[mom2] = mom[mom2],mom[mom1]
    return mom
mom = [65,565,64,454,56,454,45]
mom1,mom2 = 1,3
print(mother(mom,mom1,mom2))

gell = [5,45,43,54,434,344]
print(gell)
gell.sort()
print("list in a highest number :",gell[-1])
print("print in a smallest number in a list:",gell[0])

#inter change element places

def house(all1,all2,all3):
    all1[all2],all1[all3] = all1[all3],all1[all2]
    return all1
all1 = [23,34,65,44]
all2,all3 = 0,3
print(house(all1,all2,all3))

#change first and laSt element

def bell(create):
    length = len(create)
    toll = create[0]
    create[0] = create[length-1]
    create[length-1] = toll
    return

def multiply(list):
    result = 1
    for k in list:
        result = result * k
    return result
list1 = [1,2,3]
list2 = [2,3,4]
print(multiply(list1))
print(multiply(list2))

def normal(lock):
    toy = 0
    for t in range(0,len(lock)):
        toy = toy +lock[t]
    return toy
lolly = [1,2,3,4,5]
print(normal(lolly))

got = [-2,-3,-5,6,3,2]
for g in got:
    if g >= 0:
        print(g,end=" ")

fot =  [5,6,4,3,-7,-4,-8,-9]
for box in fot:
    if box <= 0:
        print(box,end=" ")

folk = [3,4,5,6]
print(folk)
folk.sort()
print(folk[-1])

goal = [4,5,3,25]
print(goal)
goal.sort()
print(goal[0])

def got(hgh):
    though = 1
    for fold in hgh:
        though = though*fold
    return though
vol = [3,4,6]
vol1 = [4,3,2]
print(got(vol))
print(got(vol1))

rough = [2,3,4,5,6]
print(rough)
rough.reverse()
print(rough)

def opp(oppsitive):
    could = 0
    for tolk in range(0,len(oppsitive)):
        could = could+oppsitive[tolk]
    return could
cell = [2,23,4,5]
print(opp(cell))

