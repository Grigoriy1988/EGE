# (x ∉ P) ∧ (x ∈ Q) → (x > A)
from itertools import combinations


def f(x):
    P = 5 <= x <= 54
    Q = 50 <= x <= 93
    A = a1 <= x <= a2
    return ((not P) and (Q)) <= A


Ox = [i for i in range(0, 100)]
dx = []  # длинны отрезка а
for a1, a2 in combinations(Ox, 2):
    # print(a1,a2)
    if all(f(x) == 0 for x in Ox):
        dx.append(a2 - a1)
print('\n'.join(str(i) for i in dx))
