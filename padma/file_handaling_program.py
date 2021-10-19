goof = open("reddymalapti","w+")
print(goof.write("i love so much mom"))

print(goof.read())
for poker_face in goof:
    print("print poker face :",poker_face)

reddy = open("a.txt","r+")
print(reddy.read())
print(reddy.tell())
reddy.seek(23)
print("print seek position :",reddy.read())
g = reddy.truncate(12)
print(g)

holder = open("colum","w+")
print("print holder:",holder.write("i like so much my face \n"
                                   "what are you doing  \n"
                                   "i hope you well"))
print("print read line:",holder.seek(12))
print("print seek method:",holder.write("i told you right now"))
print("print tell  count operation:",holder.tell())
got = holder.truncate(12)
print("print truncate operation : ",holder)
g= open("colum","a+")
print(g.write(" i saw yesterday she smoke well"))
g.seek(0)
#print(g.readline())
for i in g.read():
    print(i)

with open("colum") as v:
    print(v.read())

# text=["\nHello","\nHi","\nPython"]
# my_file=open("rktest.txt",mode="a+")
# my_file.writelines(text)
# print("where the file cursor is:",my_file.tell())
# my_file.seek(0)
# for line in my_file:
#       print(line)