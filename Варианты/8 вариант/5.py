def f(n):
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    d = int(n[3])
    if a*b > c*d:
        return int(str(c*d) + str(a*b))
    return int(str(a * b) + str(c * d))
res = []
for i in range(1000,10000):
    if f(str(i))==1214:
        res.append(i)
print(max(res))
