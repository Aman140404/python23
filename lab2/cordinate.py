x = int(input("enter the X cordinate"))
y = int(input("enter the Y cordinate"))

if x > 0 and y > 0:
    print("first coordinate")
elif x < 0:
    print("second quadrant")
elif x < 0 and y < 0:
    print("third quadrant")
elif x > 0 and y < 0:
    print("forth quadrant")
else:
    print("the point is in origin")
