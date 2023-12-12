def htftcm(f, i):
    cm = 0
    cm = 30.48*f
    cm = cm+(2.54*i)
    return cm


print(htftcm(5, 3))
