def div(x):
    return sorted({k for i in range(2, int(x ** 0.5) + 1) if x % i == 0 for k in (i, x // i)})


for i in range(81234, 134689 + 1):
    d  =div(i)
    if len(d) == 3:
        print(*d)
