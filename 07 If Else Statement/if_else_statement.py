#simple if statement

num = 20

if num == 20:
    print("number is 20")

#if else statement

if num > 30:
    print("number is greater than 30")
else:
    print("number is less than 30")

#nested if statement

if num < 30:
    if num%2 == 0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is greater than 30")

# if-elif statement

letter = input("Enter any letter between 'a' to 'z' :- ")
if letter == 'a':
    print("This is a vowel a")
elif letter == 'e':
    print("This is a vowel e")
elif letter == 'i':
    print("This is a vowel i")
elif letter == 'o':
    print("This is a vowel o")
elif letter == 'u':
    print("This is a vowel u")
else:
    print("letter is a consonant")