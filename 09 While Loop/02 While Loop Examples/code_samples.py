# calculate length of a list without using len() method

X = [1, 2, 3, "Python", "AI"]

length = 0
i = 0

#this code will give "IndexError: list index out of range" 
#to handle that, we will use try block
try:
    while X[i] :
        length += 1
        i +=  1
except:
    print(length)

#both the output should be same, just checking the output
print(len(X))

#print the following pattern
'''
1
22
333
4444
55555

'''

n = int(input("enter number of lines :- "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end="")
        j+= 1
    i+= 1
    print()