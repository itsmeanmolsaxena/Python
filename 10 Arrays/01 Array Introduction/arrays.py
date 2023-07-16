#array is a container tha holds multiple values of same type

from array import *

#syntax array(data_type, value_list)
a = array('i', [1,2,3,4,5])

print(a)

print(a.buffer_info())

#reverse an array
a.reverse()

print(a)

#append
a.append(10)

print(a)

#remove
a.remove(10)

print(a)