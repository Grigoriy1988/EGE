from  itertools import *
def f(x):
    p = 64 <= x <= 95
    q = 72 <= x <= 106
    a = a1 <= x <= a2
    return (q and (not a)) <= (not (p) <= (not q))
ox = [i/4 for i in range(63*4, 108*4)]
dx = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        dx.append(a2-a1)
print(min(dx))