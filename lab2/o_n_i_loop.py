m = int(input("enter the value of i loop"))
n = int(input("enter the value of j loop"))

for i in range(1, m+1, 1):
    for j in range(2, n+1, 1):
        if (j % i == 0):
            print(j, end=",")
            break
