def div(x):
    return sorted({k for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for k in (i, x // i)})

for j in range(300_000_001,300_001_001):
    d = div(j)
    if len(d)>=8:
        m = sum(x for x in d[1:8])
        if m % 2 != 0:
            print(m)