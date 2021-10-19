 # got = input("enter first number")
# print(got)
# doc = input()
# print(doc)

#opens a file for reading only

toy = open("../padma/a.txt")
print(toy.read())
g = toy.read()
print(type(g))

#it will return a list of lines

volum = open("../padma/a.txt")
print(volum.readlines())
t = volum.readlines()
print(volum)

#it reads first line

docs = open("list.py")
print(docs.readline())

# jiffy = input("first number :")
# print(jiffy)
#
ages = open("prathap")
print(ages)
ages.close()
#print(ages.read())

#
mesir = open("set_new_funtions.py")
g = mesir.read()
#
coal = open("prathap1","w")
print(coal.write("padma"))

#
coal = open("prathap1","w")
print(coal.write(g))

coal = open("prathap","a")
print(coal.write(g))

coal = open("prathap","a")
print(coal.write(g))

sumptuous = open("reddy.py","w")
print(sumptuous.write("did you reat story"))

sumptuous = open("reddy.py","w")
print(sumptuous.write("takes"))

dove = open("born","w")
print(dove.write("g"))


dove = open("read","w")
print(dove.write("reddy.going"))

done = open("prathap1","r+")
print(done.readline())
talk = done.write("house ful")
got = done.read()
print("out put :",talk)

reddy = open("padma")
print(reddy.readline())
reddy.close()

toe = open("padma","w")
print(toe.writelines(["i am an indian","joke","soul"]))
toe.close()

year = open("padma","a")
print(year.write('[" i am from","andhra pradesh","and yesterday i told to her some speech"]'))
year.close()

goal = open("padma","r+")
print(goal.readline())
vol = goal.tell()
print("tell position :",vol)
goal.seek(15,0)
vol = goal.tell()
print("tell position  print :",vol)

print(goal.writelines(" i don't like non veg"))

#truncate the file size(file size ni taggistundi)
goal.truncate(5)


print("seek position :",goal.read())
goal.close()



