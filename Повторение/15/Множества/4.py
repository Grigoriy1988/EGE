# 6599
def f(x):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)
res = []
for A in range(10000):
    if all(f(x)==1 for x in range(1,10000)):
        res.append(A)
print(min(res))