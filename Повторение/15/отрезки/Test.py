from itertools import combinations
# (¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))
def f(x):
    A = a1 <= x <= a2
    Q = 3 <= x <= 38
    P = 13 <= x <= 21
    R = 24 <= x <= 35
    return (not(Q <= (P or R))) <= ((not A) <= (not Q))

OX = [i/4 for i in range(1*4,40*4)]
dA = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) == 1 for x in OX):
        dA.append(a2 - a1)
print(dA)
print(min(dA))


