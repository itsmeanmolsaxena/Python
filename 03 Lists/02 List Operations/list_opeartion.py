mylist = [1, "This", 2, "is", 3, "a", 4, "List", 5]

#index starts from 0
#access 4th elemet of list which is string 'is' , index is 3

print(mylist[3])

#access second last elemet of list, index can be start from -1 if we are accessing list element backwards
print(mylist[-2])

#access first 3 elemet of list
print(mylist[:3])

#access element by skiping subsequent value, for ex. every odd elemet of list i.e integer only
print(mylist[::2])

#access element after 2nd element
print(mylist[2:])

#access list element by excluding first and last element
print(mylist[1:8])

#access every 3rd element in list starting from first position
print(mylist[::3])

#print list in reverse
print(mylist[::-1])

#add / concatinate two lists
conc = mylist + mylist[::-1]
print(conc)

var = list("hello world")
print(var)

#save first element in a variable and remaining elements in a seperate list
first, *other = mylist

print(first)
print(other)