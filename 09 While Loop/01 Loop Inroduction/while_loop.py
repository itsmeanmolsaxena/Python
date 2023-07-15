'''
--> a loop is an instruction that repeats multiple times as long as some condition is met

--> The while loop is used to repeat a section of code
    unknown number of times until a specific condition is met

Syntax
The syntax of a while loop is -

while expression:
    statement(s)

We can also use else with while loop

'''

#example 1

i = 1
while i <= 5:
    print(i ," Python")
    i = i+1


#example 2
i = 5
while i >= 1:
    print(i ," Python")
    i-= 1

#sum of first 10 number
i = 1
sum = 0
while i <= 10:
    sum = sum +i
    i+= 1

print(sum)

#sum of even numbers in first 10 number
i = 1
sum = 0
while i <= 10:
    if i%2 == 0:
        sum = sum +i
    i+= 1

print(sum)

#reverse a number

num = int(input("Enter any number :- "))
revnum = 0

while num % 10 != 0:
    c = num%10
    revnum = revnum*10 +c
    num = num//10

print(revnum)