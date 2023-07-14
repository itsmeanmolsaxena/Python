#set is an unordered collection of unique element
#variable_name = set([1, 2, a, b, c, 3])

s = set([1, 2, 3, 4])

print(s)
print(type(s))

s.add("a")
print(s)

#frozenset are a type of set but they are immutable means we can not modify them
fs = frozenset([1, 2, 3, 4])
print(fs)

s1 = set([1, 2, 3, 4, 5])

s2 = set([3, 4, 5, 6, 7])

#union, intersection, difference

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))