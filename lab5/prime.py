for i in range(2, 257):
    for j in range(2, 257):
        if i % j == 0:
            break
    if (i == j):
        print(i, end=",")
        