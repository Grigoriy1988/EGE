def p(x):
    return {k for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for k in (i, x // i)}

s= []
for i in range(1, 51):
    if i % 10 == 0:
        print(' '.join(str(j) for j in s))
        s.clear()
    if len(p(i)) == 2:
        s.append(i)

