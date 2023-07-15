#access element of lists

X = [1, 5., "Python"]

for i in X:
    print(i)

#print element in a range

for i in range(0,11):
    if i%2==0:
        print(i)

#This code can be converted into two lines by following way

for i in range(0,11,2):
    print(i)

#print the following pattern
'''
1
12
123
1234
12345

'''

lines = int(input("Enter number of lines:- "))

for i in range(1, lines+1):
    for j in range(1, i+1):
        print(j, end="")
    print("")