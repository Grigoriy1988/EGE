#  P = [15; 40] и Q = [21; 63])
# (¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))
from itertools import combinations
def f(x):
    P = 1023 <= x <= 2148
    Q = 1362 <= x <= 3898
    R = 1813 <= x <= 2566
    A = a1 <= x <= a2
    return (not(Q <= (P or R))) <= ((not A) <= (not Q))

Ox = [x/2 for x in range(2566*2,3898*2)]
dA = []
for a1, a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        print(a2-a1)
        dA.append(a2-a1)
print(min(dA))