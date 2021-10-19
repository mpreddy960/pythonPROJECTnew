high = 2000
try:
    g = high/0
    print(g)
# except Exception as e:
#     print(e)
except ZeroDivisionError:
    print("print")
