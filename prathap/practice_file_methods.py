drunkard = open("padma")
#print(drunkard.read())
#a = drunkard.read()
#print("read print :",a)
for reddy in drunkard.read():
    print("print reddy :",reddy)
    for talk in reddy.split():
        print("print talk :",talk)

#Python program to read file word by word

# opening the text file
with open('padma', 'r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            # displaying the words
            print("print word:",word)

#Python program to read character by character from a file


# Demonstrated Python Program
# to read file character by character

a = open("file_handaling","r")
#print("print a :",a.read())
for toy in a.read():
    print("print toy :",toy)
    for hurt in toy.split():
        print("print character to character :",hurt)

#print file method word by word
heir = open("file_handaling")
#print(heir.read())
for got in heir.readlines():
     for heires  in got.split():
         print("print data word by word :",heires)

#read line by line in text file

situation = open("file_lines")
number = situation.readlines()
print(number)
print(len(number))

