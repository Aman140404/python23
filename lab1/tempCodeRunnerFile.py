#guess the number game
#lab program 10
import random
a= random.randint(1,100)
#print(a)
for i in range(1,6,1):
    b=int(input("guess a number"))
    if(a==b):
        print("congratulations! your guess is correct...")
        break
    else:
        print("bad luck!!! try again....")