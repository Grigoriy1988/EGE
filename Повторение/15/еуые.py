def f(x):
    return ((x & 84653 != 0) or (x & 51763 != 0)) <= (x & A > 0)

res = []
for A in range(1,300_000):
    if all(f(x) == 1 for x in range(1,300_000)):
        res.append(A)

print(min(res),res)