d = {0: 'Welcome', 1: 'People', "name": {"first": "Narendra", "last": "Modi"}}
print(d)

#access any value

print(d["name"])
print(d[1])
print(d["name"]["last"])
print(d.get(0))

#delete values 

#pop method ( key is required)
print(d.pop(1))
print(d)

#popitem method ( automatially removes the last key value pair)

print(d.popitem())
print(d)

#get all values
d = {0: 'Welcome', 1: 'People', "name": {"first": "Narendra", "last": "Modi"}}
print(d.values())

#fromkeys method
keys = {'a','b', 'c', 'd'}
value = 1
d = dict.fromkeys(keys,value)

print(d)

#clear the content of dictionary

d.clear()
print(d)