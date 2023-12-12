#to calclate the grade of the student and take input of five numbers
#lab program 8
m1=float(input("enter the marks of pps"))
m2=float(input("enter the marks of pce"))
m3=float(input("enter the marks of math-2"))
m4=float(input("enter the marks of physics "))
m5=float(input("enter the marks of egd"))

per=((m1+m2 +m3+m4+m5)/500)*100
print("your percentage is:",per)
if(per>90):
    print("your grade is A+")
elif(per>80 and per<=90):
    print("your grade is A")
elif(per>70 and per<=80):
    print("your grade is B")
elif(per>60 and per<=70):
    print("your grade is C")
elif(per>50 and per<=60):
    print("your grade is D")
else:
    print("sorry you are failed")

    

