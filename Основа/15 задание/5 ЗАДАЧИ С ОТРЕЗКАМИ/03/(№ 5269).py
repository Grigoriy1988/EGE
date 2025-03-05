# P → ((Q ∧ ¬A) → ¬P)
from itertools import combinations


def f(x):
    P = 117 <= x <= 158
    Q = 129 <= x <= 180
    A = a1 <= x <= a2
    return  P <= ((Q and (not A)) <= (not P))

Ox = [i / 2 for i in range(117*2,182*2)]
dx = []
for a1, a2 in combinations(Ox,2):
    if all(f(x) == 1 for x in Ox):
        dx.append(a2 - a1)
print(min(dx))
