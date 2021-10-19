jiffy = open("file_methods")
print(jiffy.read())

piece = open("file_methods")
print(piece.readline())

press = open("file_methods")
print(press.readlines())

# talk = open("born","w")
# print(talk.write("houseful"))

sort = ["2","3"]

guts = open("born","w")
print("print write lines:",guts.writelines("123"))
guts.close()

# holl = open("born1","a")
# print(holl.write("fully furnishined"))


crone = open("born1")
#print(crone.readlines())
a = crone.tell()
print("current file positition :",a)

crone = open("born1","r+")
print(crone.readline())
crone.seek(4)
print("print seek operation",crone.readline())
a = crone.tell()
print("current file positition :",a)

crone.truncate(4)
print(crone.readline())

task = open("prathap1")
print(task.readlines())
vc = task.tell()
print("corser postition :",vc)



crone.truncate()
print("truncate pos :",crone.readline())

vow = open("tuple_new_functions.py")
print(" readline :",vow.readlines())
print("tell position :",vow.tell())

voltage = open("tuple_new_functions.py")
print(voltage.readline())
print("tell position voltage :",voltage.tell())

# cart = open("padma,"r+")
# print(cart.readline())
# print("print seek position ",cart.seek(1)
# print("print seek method :",cart.writelines("house ful"))
#

xerox = open("tuple_new_functions.py")
print(xerox.readline())

# xerox.truncate()
# print("print truncate position :",xerox.readline())

reddy = open("looping.py")
print(reddy.readlines)

holl = open("padma","w")
reddy = holl.writelines(["once","up on a time","joke"])
print(reddy)

reddy = open("sumanth","w")
print(reddy.writelines(["reddy malapati prathapreddy"]))

toll = open("got","w")
print(toll.write("high school"))

young = open("born","r")
print("print young :",young.read())

holl = open("pop","a")
print(holl.write("i talk to her"))
name = holl.tell()
print(name)
holl.close()

got = open("dox","w")
print(got.write("i talk to her"))
got.seek(23)
print(got.write("i told to her yesterday"))
got.close()

venkataravana = open("lingareddy","w")
print("print venkataravana :",venkataravana.write("i done my graduation in 2018"))
venkataravana.truncate(10)
print("truncate print :",venkataravana)



