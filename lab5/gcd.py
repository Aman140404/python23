import math


def gcd(m, n):
    c = math.lcm(m, n)
    return ((m*n)/c)


print(gcd(17, 18))
