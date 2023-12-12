n = int(input("enter a number"))
for i in range(1, n, 1):
    # print(i, end=" ")

    if i == 4:
        continue
    if i == 9:
        pass
    if i == 50:
        break
    print(i, end=" ")
