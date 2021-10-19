total = [3,4,5]
print(sum(total))
def g(right,right2):
    total = right+right2
    print(total)
    return total

g(243,243)
print("total amount :",total)


def hot(goat2,dog3):
    dog = goat2+dog3
    print('sum total:',dog)
    return dog

goat,kol = 34,43
hot(goat,kol)
print(goat,kol)

lamda = [343,343,35]
def attribute(lamda):
    lamda= {3233:4545}
    print(lamda)
    return lamda
#float = {'red cells':'white cells'}
attribute(lamda)
print(lamda)
wnet  = (1,2,3)
def go(wnet):
    wnet = {'tour':'japan'}
    print('folk:',wnet)
    return
#wne = [54,4,454,45]
go(wnet)
print('list:',wnet)

while wnet:
    print(wnet)
    break
print(wnet)
for hight in wnet:
    print(hight)

#funtion arguments

def unspec_args(a,*args):
    return "a = %s , other =%s" %(a,args)
print(unspec_args('true','full',23,55,"false"))

def unspec_args(a,**kwargs):
    return f"a = {a}, other ={kwargs}"
print(unspec_args('true',c = 'reddy'))

def unspec_args(a,*args, **kwargs):
    return f"a = {a}, other ={args,kwargs}"
print(unspec_args('true','rtrtr,ytyty,232',c = 'reddy'))

def unspec_args(a,*args, **kwargs):
    return f"a = {a}, tuple is ={args}, dictinary is :{kwargs}"
print(unspec_args('true','rtrtr,ytyty,232',c = 'reddy'))

