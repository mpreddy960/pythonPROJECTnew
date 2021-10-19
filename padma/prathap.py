#Write a Python function that accepts a string and calculate
# the number of upper case letters and lower case letters.

def h(f):
    foe = 0
    toe = 0
    for y in f:
        if y.isupper():
            foe+=1
        elif y.islower():
            toe+=1
    return foe,toe
    print("print upper case letters:",foe)
    print("print lower case letters :",toe)

reddy = "MALAPATI prathap"
print(h(reddy))




