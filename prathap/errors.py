#syntax error
#miss colon
#
# correct = 1000
# if (correct >2000)
#     print(correct)

#exceptions error
#INDEX ERROR

ready= [1,2,3]
try:
    print("second element",(ready[1]))
    print("third element ",(ready[3]))
except IndexError:
    print("print error")

doc = [23,4,3,45,43,4,44]
try:
    print("third element :",(doc[2]))
    print("print seventh element :",(doc[7]))
except IndexError:
    print("indexing error")

#traceback error

# cremate = [2,3,4,56]
# print(cremat)

tomb = {"reddy":"malapati","malapati":"venkataravana"}
print(tomb)
# try:
#     tomb[b] = "key"
#     print(tomb)
# except Exception as e:
#     print("print value error",e)

try:
    tomb[b] = "key"
    print(tomb)
except :
    print("print value error")

#NAME ERROR

#
# tomb[b] = "key"
# print(tomb)
# print("print value error")

#ZERO  DIVISION  ERROR


# # initialize the amount variable
# marks = 10000
# # perform division with 0
# a = marks / 0
# print(a)
#doc = {"high":45,"weight":67}
#print(do)

# routine = [23,2,32,4,3,"redsdt",refg]
# print(routine)
#

#file error

def counter(fname):
    # variable to store total word count
    num_words = 0

    # variable to store total line count
    num_lines = 0

    # variable to store total character count
    num_charc = 0

    # variable to store total space count
    num_spaces = 0

    # opening file using with() method
    # so that file gets closed
    # after completion of work
    with open(fname, 'r') as f:

        # loop to iterate file
        # line by line
        for line in f:

            # incrementing value of
            # num_lines with each
            # iteration of loop to
            # store total line count
            num_lines += 1

            # declaring a variable word
            # and assigning its value as Y
            # because every file is
            # supposed to start with
            # a word or a character
            word = 'Y'

            # loop to iterate every
            # line letter by letter
            for letter in line:

                # condition to check
                # that the encountered character
                # is not white space and a word
                if (letter != ' ' and word == 'Y'):

                    # incrementing the word
                    # count by 1
                    num_words += 1

                    # assigning value N to
                    # variable word because until
                    # space will not encounter
                    # a word can not be completed
                    word = 'N'

                # condition to check
                # that the encountered character
                # is a white space
                elif (letter == ' '):

                    # incrementing the space
                    # count by 1
                    num_spaces += 1

                    # assigning value Y to
                    # variable word because after
                    # white space a word
                    # is supposed to occur
                    word = 'Y'

                # loop to iterate every
                # letter character by
                # character
                for i in letter:

                    # condition to check
                    # that the encountered character
                    # is not  white space and not
                    # a newline character
                    if (i != " " and i != "\n"):
                        # incrementing character
                        # count by 1
                        num_charc += 1

    # printing total word count
    print("Number of words in text file: ", num_words)

    # printing total line count
    print("Number of lines in text file: ", num_lines)

    # printing total character count
    print('Number of characters in text file: ', num_charc)

    # printing total space count
    print('Number of spaces in text file: ', num_spaces)
# Driver Code:
if __name__ == '__main__':
    fname = 'File1.txt'
    try:
        counter(fname)
    except Exception as nema:
        print('File not found',nema)

#permission error

# toll = open("reddy")
# print(toll.read())

high = {"height":177,"weight":67}
print(high)
try:
    high["reddy"] = malapati
except NameError:
    print("print error",high)

#indexing error and handiling

toll = [23,34,34,345]
print(toll)
try:
    print(toll[5])
except IndexError:
    print("indexing error ",toll)

# arithematic error
#zero division error

# try:
#     a = 10/0
#     print(a)
# except ZeroDivisionError:
#     print (a)


# visible = {"math":45,"pysics":56}
# print(visible)
# print(visible["chemistry"])


def reddy(full,t):
    if(full>t):
        return full
    return t
r =1
t = 2
print(reddy(r,t))


def reddy(full,t):
    if(full>t):
        return full
    return t
r =1
t = 2
f = 6
print(reddy(t,reddy(r,f)))


from module import *
did = dox("force")
print(did)


