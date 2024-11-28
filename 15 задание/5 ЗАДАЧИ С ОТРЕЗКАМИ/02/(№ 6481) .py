# (¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))
# (¬(Q → (P ∨ R))) → (¬A → ¬Q)
from itertools import combinations


def f(x):
    P = 106 <= x <= 218
    Q = 132 <= x <= 388
    R = 183 <=x<=256
    A = a1 <= x <= a2
    return (not(Q <= (P or R))) <= ((not A) <= (not Q))


Ox = [i /2 for i in range(100*2, 390*2)]
dx = []  # длинны отрезка а
for a1, a2 in combinations(Ox, 2):
    # print(a1,a2)
    if all(f(x) == 1 for x in Ox):
        dx.append(a2 - a1)
# print('\n'.join(str(i) for i in dx))
print(min(dx))