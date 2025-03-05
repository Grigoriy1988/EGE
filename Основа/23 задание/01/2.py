a = [0]*16
a[1] = 1
for i in range(1,15):
    if i + 1 <= 15:
        a[i+1] += a[i]
    if i + 3 <= 15:
        a[i+3] += a[i]
    if i * 2 <= 15:
        a[i*2] += a[i]
print(a)