'''
a function is a set of code that performs some task
syntax for function
def function name:
    statement(s)
'''

def welcome():
    print("Good Morning")

#function call
welcome()

#add two numbers

def add(a, b):
    print(a+b)

add(10,20)

#add two numbers, parameters should have a default value

def add(a=0, b=0):
    print(a+b)

add(10)
add(10,34)

# add multiple numbers, *a denotes a list

def add(*a):
    total = 0
    for i in a:
        total = total + i
    print("The sum is :- ", total)

add(10, 20, 30, 40)
add(1, 2, 3)


# call by reference example

def add(a, b):
    print(id(a), id(b))
    a = 2
    b = 3
    print(id(a), id(b))
    total = a + b
    print("Total is :- ", total)

x = 10
y = 20

print(id(x), id(y))
add(x,y)
print("the sum is = ", x+y)

# return keyword

def add(a, b):
    total = a+b
    return total


sum = add(20,30)
print(sum)