def revsum(a):
    rev = 0
    sumnum = 0
    while (a > 0):
        udig = a % 10
        sumnum = sumnum+udig
        rev = rev*10+udig
        a = a//10
    return ("reverse of the number is ", rev, "\nthe sum of the digits of the number is ", sumnum)


print(revsum(123))
