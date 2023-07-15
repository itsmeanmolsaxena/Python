X = []
Y = []
val = []
sum = []

#works for same number of rown and column

r = int(input("enter number of rows :- "))
c = int(input("enter number of columns :- "))

for i in range(0,r):
    for j in range(0, c):
        val.insert(j, int(input("enter %d * %d element :- " %(i,j))))

    X.insert(i, val)
    val = []
    
for i in range(0,r):
    for j in range(0, c):
        val.insert(j, int(input("enter %d * %d element :- " %(i,j))))
        
    Y.insert(i, val)
    val = []

for i in range(0,r):
    for j in range(0,c):
        val.insert(j, X[i][j] + Y[i][j])
    sum.insert(i,val)
    val =[]

print(sum)