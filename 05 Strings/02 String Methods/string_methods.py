stg = "Hello, We are learning Python."

#uppercase, lowercase
print(stg.upper())
print(stg.lower())

#find any character's index
#both the methods return the very first occurance

print(stg.find("P"))
print(stg.index("P"))

#convert string to list , each word in string is seperated by space
#space will be a Delimiter here
print(stg.split(" "))

#replace any value in string
print(stg.replace("Python", "Data Science"))

#convert tring to tuple, everything before and after " are " is an element of tuple
print(stg.rpartition(" are "))

#add two strings
stg1 = "Hi"
stg2 = "All"

print(stg1+" "+stg2)

#add multiple strings using format
stg1 = "Hi"
stg2 = "All"
stg3 = "There"

#{} is placeholder and in whichever format we provide them in double quoyes, they are stored in a variable
stg = "{} {}, {}".format(stg1, stg2, stg3)

print(stg)
