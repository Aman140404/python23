#lab programm 4
#to check the largest number among three numbers
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))

if(num1>num2):
    if(num1>num3):
        print("the largest number is ",num1)
    else:
        print("the largest number is ",num3)
else:
    if(num2>num3):
                print("the largest number is ",num2)
    else:
                print("the largest number is ",num3)
if(num1<num2):
    if(num1<num3):
        print("the smallest number is ",num1)
    else:
        print("the smallest number is ",num3)
else:
    if(num2<num3):
                print("the smallest number is ",num2)
    else:
                print("the smallest number is ",num3)




