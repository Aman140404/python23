a = []
for i in range(0, 10):
    num = int(input("enter the element"))
    a.append(num)
lar = a[i]
for i in range(0, 10):
    if (a[i] > lar):
        lar = a[i]
print("the largest element is ", lar)
sam = a[i]
for i in range(0, 10):
    if (a[i] < sam):
        sam = a[i]
print("the smallest element is ", sam)
