from itertools import combinations


# (( not Q and (P ∨ R))) and (A and ¬Q)
def f(x):
    P = 1023 <= x <= 2148
    Q = 1362 <= x <= 3898
    R = 1813 <= x <= 2566
    A = a1 <= x <= a2
    return ((not Q) and (P or R)) and (A and (not Q))


Ox = [i for i in range(1022, 3899)]
dx = []  # длинны отрезка а
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        # print(a2-a1)
        dx.append(a2 - a1)
print(min(dx))
# print('\n'.join(str(i) for i in dx))
