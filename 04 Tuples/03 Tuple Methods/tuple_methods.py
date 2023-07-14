mytuple = (1, 2, 3, 4, 5, 1, 6, 1, 7, 2, 8, 2, 9)

#count method
print(mytuple.count(2))

#length , max and minimum, addition in tuple
print("Length of Tuple :-",len(mytuple))
print("Minium value in Tuple :-",min(mytuple))
print("Maximum value in tuple :-",max(mytuple))
print("sum of the tuple :-",sum(mytuple))

#convert list to tuple
list_1 = [1, 2, 3, 4, 5]
print(list_1)

tuple_1 = tuple(list_1)
print(tuple_1)

#nesting of lists in a tuple

tuple_1 = ([1,2,3], [5,6,7], [8,9,10])

#tuples are immutable but list inside a tuple is mutble

tuple_1[0].append(4)

print(tuple_1)

