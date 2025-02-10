n = int(input())
x = int(input())
if x == 0:
    r = 0
else:
    r = x % n
    if r > n - r:
        r = n - r

print(r)
