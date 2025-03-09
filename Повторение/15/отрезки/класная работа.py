# 8009
from itertools import combinations


# ¬(x ∈ A) ∨ (¬(x ∈ B) ∧ ¬(x ∈ C) ∧ ¬(x ∈ D))
def f(x):
    A = a1 <= x <= a2
    B = 3 <= x <= 49
    C = 0 <= x <= 5
    D = 43 <= x <= 123
    return (not A) or ((not B) and (not C) and (not D))


Ox = [i  for i in range(0 , 993  + 1)]
dA = [] # длинны отрезка а
for a1,a2 in combinations(Ox,2):
    if all(f(x) == 1 for x in Ox):
        # print(a2-a1)
        dA.append(a2 - a1)
print('\n'.join(str(i) for i in dA))
print(max(dA))


