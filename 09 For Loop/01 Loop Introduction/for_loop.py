'''
--> a loop is an instruction that repeats multiple times as long as some condition is met

--> for loop is used to iterate over a sequence, which could be a list, tuple, array or string 

For Loops Syntax

for COUNTER in SEQUENCE:
    # statements

'''

#for loop in list

X = [1, 2, 3, 'a', 'b', 'c']
for i in X:
    print(i, end="")

print("\n-------------\n")
#for loop in string

X = "Python"
for i in X:
    print(i, end="")

print("\n-------------\n")
#nested for loop 

X = [[8, 9, 10], ['x', 'y', 'z']]

for i in X:   
    for j in i:   
        print(j, end="")

'''
Python For Loop inside a For Loop

This code uses nested for loops to iterate over both the lists inside X, and prints the 
value of i and j for each combination of the two loops. The inner loop is executed for 
each value of i in the outer loop. The output of this code will print the numbers 8, 9, 10
as each value of i is combined with each value of j. Then in second iteration, it will print 
x, y, z.
'''

print("\n-------------\n")
#break statement

X = "Hey there, how are you?"

for i in X:
    if i == ",":
        break
    print(i, end="")


print("\n-------------\n")
#continue statement

X = [1, 13, 34, 56, 10]

for i in X:
    if i > 10:
        continue
    print(i)
