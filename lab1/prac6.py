
num =int(input("enter a number to check armstrong of not"))
num1=num
num2=num
count=0
while num1>0:
    num1=int(num1/10)
    count=count+1
    
arm=0
while num>0 :
    udig=num%10
    arm=arm+pow(udig,count)
    num=int(num/10)
if(arm==num2):
    print("number is armstrong")
else:
    print("number is not armstrong")
