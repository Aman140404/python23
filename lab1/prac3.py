#lab practical 3
#to input a  number from the user and check the folloiwng conditions
num=int(input("enter a number"))
if(num%2!=0):
    print("weird")
else:
    if(num>=2 and num<=5):
        print("not weird")
    if(num>=6 and num<=20):
        print("weird")
    if(num>20):
        print("not weird")
        
