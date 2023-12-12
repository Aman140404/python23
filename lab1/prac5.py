#lab program 5
#to check number is perfect or not
num=int(input("enter a number"))
count=0
for i in range(1,num,1):
    if(num%i==0):
        count=count+i
if(count==num):
    print("the entered number is a perfect number")
else:
    print("the entered number is not a perfect number")
