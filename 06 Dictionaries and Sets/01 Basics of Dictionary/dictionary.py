#dictionary is an unordered collection of data stored in a key value pair

#syntax
#variable_name = {key1 : value2, key2 : value2...}

#there are diferent types to create a dictionary

d1 = {1:"Hello", 2:"World!"}

d2 = {"name":"Ram", "brother":"Bharat" }

d3 = dict({1:"Hello", "name":"Ram"})

d4 = dict([("name","Ram"), (2,"God")])

d5 = {"name": {"first": "Narendra", "last": "Modi" }, "age": 65, "party":"BJP"}

print(d1, "\n", d2, "\n", d3,"\n", d4, "\n", d5)

#add an element in list

d={}
d[0]= "Welcome"
print(d)

d[1]= "People"
print(d)

#add a tuple as a value
d["tuple"] = ("This", "is", "a", "tuple", "as", "a", "value")
print(d)

#update the tuple value

d["tuple"] = ("This is a tuple", "updated")
print(d)