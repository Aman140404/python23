def numfive(n):
    a = {}
    s = posum = negsum = 0
    for i in range(0, n):
        a[i] = int(input("enter the element"))
    for i in range(0, n):
        s = s+a[i]
        if (a[i] > 0):
            posum = posum+a[i]
        else:
            negsum = negsum+a[i]
    avg = s/n
    for i in range(0, n):
        if (a[i] > avg):
            print(a[i], "is greater than average")
    # print("\nthe number greater than the average is ")
    # for i in range(0, n, 1):
    #     if (a[i] > avg):
    #         (a[i])

    return (negsum, posum)


print(numfive(5))
