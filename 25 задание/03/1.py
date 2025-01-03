def div(x):
    return sorted({k for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for k in (i, x // i)})
for i in range(154026, 154043 + 1):
    d = div(i)
    if len(d) == 4:
        print(f'{d[2]} {d[3]}')