n = int(input("enter the number to find no of steps required=>"))
count = 0
n1 = n
while (n > 0):
    if n % 2 == 0:
        n = n//2
        count = count+1
    else:
        n = n-1
        count = count+1
print("The number of steps required to reduce", n1, "into 0 is", count)
