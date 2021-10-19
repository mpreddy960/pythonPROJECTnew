#Python – Extract Unique values dictionary values
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print("The original dictionary is : " + str(test_dict))
#res = list(sorted({ele for val in test_dict.values() for ele in val}))
result = set()
for value in test_dict.values():
    for element in value:
        result.add(element)
print("unique values :",result)
#print("The unique values list is : " + str(res))

#practice

got = {"break":[332,33,3434],"god":[33,453,3434]}
print("original dictionary:",got)
focus = set()
for cell in got.values():
    for doc in cell:
        focus.add(doc)
print("unique values in a dictionary :",focus)
print("sorted values in a dictionary :",sorted(focus))

#practice

confidence = {"got":[2,3,4,54,3,4,3],"folk":[4,5,3,4,5,8],"sold":[12,34,45,65]}
print("the original ditionary :",confidence)
court = list(({ele for val in confidence.values() for ele in val}))
print("the unique values list is :",court)

#Python program to find the sum of all items in a dictionary

def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum
# Driver Function
mydict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(mydict))

#practice

def google(ground):
    folk = 0
    for holi in ground:
        folk = folk+ground[holi]
    return folk
#driver code lo edaina  varialble name evvavochchu
ground = {"toll gate":564,"marks":36}
print(google(ground))

#Python | Ways to remove a key from dictionary

test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
# Printing dictionary before removal
print("The dictionary before performing remove is : " + str(test_dict))
# Using del to remove a dict
# removes Mani
del test_dict['Mani']
# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
# Using del to remove a dict
# raises exception
#del test_dict['Manjeet']

#Ways to sort list of dictionaries by values in Python – Using lambda function

# lis = [{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 20},
#        {"name": "Nikhil", "age": 19}]
#
# # using sorted and lambda to print list sorted
# # by age
# print
# "The list printed sorting by age: "
# print
# sorted(lis, key=lambda i: i['age'])
#
# print("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# # now comes before "Nandini"
# print
# "The list printed sorting by age and name: "
# print
# sorted(lis, key=lambda i: (i['age'], i['name']))
#
# print("\r")
#
# # using sorted and lambda to print list sorted
# # by age in descending order
# print
# "The list printed sorting by age in descending order: "
# print
# sorted(lis, key=lambda i: i['age'], reverse=True)

#Python | Merging two Dictionaries

def Merge(dict1,dict2):
    return (dict2.update(dict1))
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
# This return None
print("merging two ditionaries :",Merge(dict1, dict2))
# changes made in dict2
print(dict2)

def merging(come1,come2):
    return come2.update(come1)
come1 = {"goal":"achivment","tiger":"animal"}
come2 = {"sold":"cloth","cell":"blood cell"}
print("merging two ditionarys :",merging(come1,come2))
print("print merging two dictionarys:",come2)

def blue(*goal):
    return goal
f = [54,4545,454]
g = [55,4545,445]
print(blue(f,g))

#practice
def going(come1,come2):
    return (come2.update(come1))
come1 = {"hot":"milk","cold":"water","sweet":"laddu"}
come2 = {"toy":"doll","gel":"shower"}
print(going(come1,come2))
print(come2)

#pratice

def fell(save1,save2):
    return (save1.update(save2))
save1 = {"pincode":523327,"numbers":56,"lucky numbers":4}
save2 = {"god":"soul","blessings":"mother"}
print("merging two dictionary:",fell(save1,save2))
print("merging dictionaries :",save1)



def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

#pratice

def argue(fold1,fold2):
    drug = {**fold1,**fold2}
    return drug
fold1= {"alphabet":98,"future":75}
fold2= {"quantity":67,"chemistry":56}
fold3 = argue(fold1, fold2)
print(fold3)

#type1

def Merge(dict1 ={'x': 10, 'y': 8}, dict2 ={'a': 6, 'b': 4}):
    res = dict1,dict2
    return res
#dict1 = {'x': 10, 'y': 8}
#dict2 = {'a': 6, 'b': 4}
dict3 = Merge()
print(dict3)

#PRACTICE

def blue(goal1,goal2):
    count = goal1,goal2
    return count
goal1 = {"cart":"ecart","high":"level","low":"battery"}
goal2 = {"soul":"god","noun":"names","correct":"roung"}
alternative = blue(goal1,goal2)
print(alternative)

#Python – Append Dictionary Keys and Values ( In order ) in dictionary

test_dict = {"Gfg": 1, "is": 3, "Best": 2}
print("print keys dictionary :",test_dict.keys())
print(list(test_dict.keys()))
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
# + operator is used to perform adding keys and values
res = list(test_dict.keys()) + list(test_dict.values())
# printing result
print(res)

#practice

fortune = {"animal":"baffelo","dairy":"farm"}
print("original dictionary :",fortune)
plants = list(fortune.keys())+list(fortune.values())
print("ordered keys and values :",plants)
#Python | Sort Python Dictionaries by Key or Value

# Function calling
#def dictionairy():
    # Declare hash function
key_value = {}
# Initializing value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
print("Task 1:-")
print("Keys are")
# iterkeys() returns an iterator over the
# dictionary’s keys.
for i in sorted(key_value.keys()):
    print(i, end=" ")
#def main():
    # function calling
 #  dictionairy()
# Main function calling
#if __name__ == "__main__":
 #   main()

#practice sorted

tecnical = {}
tecnical["guidence"] = "correct way"
tecnical["weakness"] = "tried"
tecnical["god"] = "blessings"
tecnical["forest"] = "animals"
print("print tecnical dictionary :",tecnical)
for true in sorted(tecnical.keys()):
    print(true, end= "  ")

pour = {"water":"hot","milk":"boiled","cloth":"tea shirt"}
print(pour)
spinkle = sorted(pour.keys())
print(spinkle)

#Python – Sort Dictionary key and values List

test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}
print(test_dict["gfg"])
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])
# printing result
print("The sorted dictionary : " + str(res))

#for key in

#practice

covered = {"routine": [3,4,56,53],"common": [7,6,4],"government": [4,6,5,7]}
print(covered)
sortedvalues = dict()
for key in sorted(covered):
    sortedvalues[key] = sorted(covered[key])
print("print sorted values :",sortedvalues)

#practice

food = {"quality":"good","cloth":"striching","distance":56}
print(food)
fod = dict()
for key in sorted(food):
    print(sorted(food))

def good(foolish):
    return foolish
foolish  = {"english":"teachwer","telugu":"medam"}
print(good(sorted(foolish)))



test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()
res = {key: sorted(test_dict[key]) for key in sorted(test_dict)}

# printing result
print("The sorted dictionary : " + str(res))

#Handling missing keys in Python dictionaries

country_code = {'India': '0091',
               'Australia': '0025',
               'Nepal': '00977'}
# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))
# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))

#practice : 1

all_countries = {"india":"culture","america":"bad culture","japan":"poor country"}
print(" print original data :",all_countries)
print("get keys :",all_countries.get("india","no data"))
print("missing  data printing :",all_countries.get("south africa","not availeble data"))

#practice : 2

all_distict_codes = {"praksham":523327,"guntur":523314,"karnool":654443}
print(all_distict_codes)
print(all_distict_codes.get("karnool","not availble"))
print(all_distict_codes.get("narasaraopet","no data"))


doc = {"kettle":"botle","zoo":"animal"}
print(doc)
fold = {"road":5}
print(fold.update(doc))
print(fold)
doc[3] = 45
print(doc)
print(doc.keys())
for i in doc.keys():
    print(i)
doc = {"gold":20,"got":"marks"}
print(doc)
doc["true"]= "false"
print(doc)

docs = {"maths":65,"physics":70}
print(docs)
dox = {"speed":70,"number":100}
print(dox)
docs.update(dox)
print(docs)

for i in sorted(docs.keys()):
    print(i,end=' ')

#Python | Convert a list of Tuples into Dictionary

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))

god = {"toll":[8,4,5],"mood":[5,4,3],"set":[8,9,10],"told":[8,10]}
print("print dictionary",god)
sold = set()
for dove in god.values():
    for goal in dove:
        sold.add(goal)
print("unique values in a dictionary:",sold)




animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"}

outDict = {key: animaldict[key] for key in ["name", "age"]}
print(outDict)
fog = dict()
for key in ['name','age']:
    print(animaldict[key])



# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
print(list(sorted(marks.keys())))

house = {}.fromkeys(["folder","formhouse","formula"],23)
print(house)

for holi in house.items():
    print(holi)
print(list(sorted(house.keys())))

box = {"mobile":"sigle","month":3,"force":"boll"}
print(box)
box["count"] = 23
print("adding a key value",box)

#how to addede in list element to dictionary

vow = {}.fromkeys([23233,34,545],5)
print(vow)

for got in vow.items():
    print(got)

correct = {"mesir":2,"stigy":34,"tetoller":45}
print(correct)
for _ in correct:
    print("print dictionary :",_)

animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"
}
outDict = {key: animaldict[key] for key in animaldict.keys() - ["name", "age"]}
print(outDict)

#How to change the name of key in dictionary.

animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"
}
#practice

animaldict['Animalname'] = animaldict.pop('name')
print(animaldict)

xerox = {"enter":"application form","counter":5,"level":23}
print(xerox)
xerox["talking tom"] = xerox.pop("enter")
print(xerox)

animaldict = {
    "animal": {
        "name": "Dog",
        "age": 5,
    },
    "animal1": {
        "name": "Cat",
        "age": 2,
    },
    "animal2": {
        "name": "Rabbit",
        "age": 1,
    },
}
animaldict["animal1"]['age'] = 5
print(animaldict)

fruitsDict = {
    'Apple': 100,
    'Orange': 200,
    'Banana': 400,
    'pomegranate': 600
}
if 'Apple' in fruitsDict:
    del fruitsDict['Apple']
print('Dict after deleting key =', fruitsDict)

prodigal = {"grey":34,"blue":67,"yellow":34,"red":57}
if "blue" in prodigal:
    del prodigal["blue"]
print(prodigal)

