mat = int(input("enter your marks in maths:"))
phy = int(input("enter your marks in physics:"))
chem = int(input("enter your marks in chemistry:"))
if mat >= 65 and phy >= 55 and chem >= 50 and (mat+phy+chem) >= 190 or (mat+phy >= 140):
    print("congratulations you are eligible for admission")
else:
    print("sorry you are not eligible to take admission")
