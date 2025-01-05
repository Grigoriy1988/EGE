def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


a = 250200 + 1
for i in range(a, a + 2000):
    D = div(i)
    S = max(D) + min(D) if len(D) > 0 else 0
    if S != 0 and S % 123 == 17:
        print(i, S)
