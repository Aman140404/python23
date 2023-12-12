#to check wheather the number is prime or not


flag=0
#ch='y'
#while(ch=='y'):
num=int(input("enter a positive number"))
for i in range(2,num,1):
        if(num%i==0):
            flag=1
            break
if(flag==1):
              print("the",num ,"is not a prime number")
else:
              print("the",num,"is a prime number")
    #ch=input("do you want to check another number")
    
