mylist = [1, "This", 2, "is", 3, "a", 4, "List", 5]

#append method

mylist.append(".")
print(mylist)

#add an entire list into the given list i.e extend method

new_list = [6, "This", 7, "is", 8, "extended", 9, "list", 10]

mylist.extend(new_list)

print(mylist)

#remove any element in list ( only remove only first occureance)
mylist.remove('.')
print(mylist)

#insert any element in the list
mylist.insert(9, "and")
print(mylist)

#sort any list
random = [54, 65, 3, 56, 23, 78, 89, 65]
random.sort()
print(random)

#length , max and minimum, addition in list
print(len(random))
print(min(random))
print(max(random))
print(sum(random))
