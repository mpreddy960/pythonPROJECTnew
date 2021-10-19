#Example 1: Program to print half pyramid using *

rows = 5
for i in range(rows):
    #print("print i :",i)
    for j in range(i+1):
       # print("print j:")
        print("* ", end="")
    print("\n")

row = 3
for ih in range(row):
    for j in range(ih+1):
        print("* ",end= "")
    print("\n")


line = 6
for g in range(line):
    for v in range(g+1):
        print("* ",end="")
    print("\n")
    
# #Example 2: Program to print half pyramid a using numbers
#
# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print("\n")
#
# #Example 3: Program to print half pyramid using alphabets
#
# rows = 5
#
# ascii_value = 65
#
# for i in range(rows):
#     for j in range(i + 1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")
#
#     ascii_value += 1
#     print("\n")
#
# #Example 4: Inverted half pyramid using *
#
# rows = 5
#
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
#
#     print("\n")
#
# #Example 5: Inverted half pyramid using numbers
#
# rows = 5
#
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#
#     print("\n")
#
# #Example 6: Program to print full pyramid using *
#
# rows = 5
#
# k = 0
#
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#
#     k = 0
#     print()
#
# #Example 7: Full Pyramid of Numbers
#
# rows = 5
#
# k = 0
# count = 0
# count1 = 0
#
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print("  ", end="")
#         count += 1
#
#     while k != ((2 * i) - 1):
#         if count <= rows - 1:
#             print(i + k, end=" ")
#             count += 1
#         else:
#             count1 += 1
#             print(i + k - (2 * count1), end=" ")
#         k += 1
#
#     count1 = count = k = 0
#     print()
#
# #Example 8: Inverted full pyramid of *
#
# rows = 5
#
# for i in range(rows, 1, -1):
#     for space in range(0, rows-i):
#         print("  ", end="")
#     for j in range(i, 2*i-1):
#         print("* ", end="")
#     for j in range(1, i-1):
#         print("* ", end="")
#     print()
#
# #Example 9: Pascal's Triangle
#
# rows = 3
# coef = 1
#
# for i in range(1, rows+1):
#     for space in range(1, rows-i+1):
#         print(" ",end="")
#     for j in range(0, i):
#         if j==0 or i==0:
#             coef = 1
#         else:
#             coef = coef * (i - j)//j
#         print(coef, end = " ")
#     print()
#
# #Example 10: Floyd's Triangle
#
# rows = 3
# number = 1
#
# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print(number, end=" ")
#         number += 1
#     print()

