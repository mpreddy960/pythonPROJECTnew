let = {"meet":"cm","look":"handsome","move":"out side","pass":75}
print(let)
print(let.values())
print(let.keys())
print(len(let))
print(let.items())
print(let.popitem())
print(let)
reddy = {"math":34,"pysics":56}
print(reddy.update(let))
print(reddy)
print(reddy.keys())
reddy = {2:"key"}
print(reddy.update(let))
print(reddy)
d = {1: "one", 2: "three"}
d1 = {2: "two"}
# updates the value of key 2
d.update(d1)
print(d)
d1 = {3: "three"}
# adds element with key 3
d.update(d1)
print(d)
d["numeric"] = "i watch tv"
d["house"] = "our own house"
d["best fiend"] = "i like sports"
print("updating  a dictionary :",d)


prathapreddy = {"maths":"56","history":"89","economics":"45"}
print(prathapreddy)
print(prathapreddy.keys())

g = (str(d))
print(g)
print(type(g))
print(g.find("house"))

a = "history"
for i in prathapreddy:
    if i == a:
        print("exstis key value :",i,prathapreddy[i])
    else:
        print("no  key value exists in a ditionary :")







