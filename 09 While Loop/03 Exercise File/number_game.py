import random

nump = random.randint(10,99)
n = int(input("please enter a 2 digit number :- "))

while n != 10:
    num = nump
    cor = 0
    while num % 10 != 0:
        numc = n%10
        nc = num%10
        num = num//10
        n = n//10
        if numc == nc:
            cor = cor + 1
    if cor == 2:
        print("Congrats, you guessed it right")
        break
    else:
        print("%d digit were guessed right" %cor)
        n = int(input("please enter a 2 digit number :- "))
else:
    print("you quit the game")