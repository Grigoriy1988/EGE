a = [0] * 24
a[23] = 1
for i in range(23, 2, -1):
    if i - 2 >= 2:
        a[i - 2] += a[i]
    if i - 5 >= 2:
        a[i - 5] += a[i]
print(a)
