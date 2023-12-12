npov = 0
nnev = 0
while True:
    n = int(input("enter a number"))
    if (n == 0):
        break
    elif (n > 0):
        npov = npov+1
    else:
        nnev = nnev+1
print("number of negative number enterd=>", nnev)
print("number of positive number entered=>", npov)
