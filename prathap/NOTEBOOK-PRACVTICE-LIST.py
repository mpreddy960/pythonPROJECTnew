def swaplist(newlist):
    length = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[length-1]
    newlist[length-1] = temp
    return newlist
nnewcolon = [1,2,3,4,5,6]
print(swaplist(nnewcolon))

def despair(wash,wash1,wash2):
    wash[wash1],wash[wash2] = wash[wash2],wash[wash1]
    return wash
wash = [12,14,16,18,20]
wash1,wash2 = 0,3
print("chage in a list elements places :",despair(wash,wash1,wash2))

stingy = [1,2,3,4,5,6,7,8]
print(stingy)
stingy.sort()
print("print highest number in a list:",stingy[-1])

miser = [1,2,3,4,5,6,7,8]
print(miser)
miser.sort()
print("print smallest number in a list :",miser[0])

for fold in miser: