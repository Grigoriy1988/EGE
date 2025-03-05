def div(x):
    d = {k for i in range(2, int(x**0.5) + 1) if x % i == 0 for k in (i, x// i)}
    return sorted(d)

for i in range(174457, 174505+1):
    d = div(i)
    if len(d) == 2:
        print(f'{d[0]}\t{d[1]}\t{d[0]*d[1]}')

