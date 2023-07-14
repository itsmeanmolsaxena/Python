mytuple = [1, "This", 2, "is", 3, "a", 4, "Tuple", 5]

#index starts from 0
#access 4th elemet of tuple which is string 'is' , index is 3

print(mytuple[3])

#access second last elemet of tuple, index can be start from -1 if we are accessing tuple element backwards
print(mytuple[-2])

#access first 3 elemet of tuple
print(mytuple[:3])

#access element by skiping subsequent value, for ex. every odd elemet of tuple i.e integer only
print(mytuple[::2])

#access element after 2nd element
print(mytuple[2:])

#access tuple element by excluding first and last element
print(mytuple[1:8])

#access every 3rd element in tuple starting from first position
print(mytuple[::3])

#print tuple in reverse
print(mytuple[::-1])

#add / concatinate two tuples
conc = mytuple + mytuple[::-1]
print(conc)

#nesting of tuples
nest = (mytuple[1::2], mytuple[::2] )
print("Nested tuples is :-", nest)

# repeatition
rep = ("Good",)*10
print(rep)

#operation performed in print statement will not modify the original tuple
rep1 = ("Good",)
print(rep1*10)
print(rep1)

#save first element in a variable and remaining elements in a seperate tuple
first, *other = mytuple

print(first)
print(other)

#other variable holds elements of tuple in a form of list

#another example
num = (1, 2, 3, 4)
print(num)
a, b, c, d = num
print(a, b, c, d)

#here, b is a list, * denotes it will be a list
a, *b , c = num
print(a, b, c)

# a tuple can be deleted by using del keyword
del conc
print(conc) # this should give an error