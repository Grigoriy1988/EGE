from itertools import combinations


# (¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))
def f(x):
    A = a1 <= x <= a2
    Q = 3 <= x <= 38
    P = 13 <= x <= 21
    R = 24 <= x <= 35
    return (not (Q <= (P or R))) <= ((not A) <= (not Q))


Ox = [i/2  for i in range(0*2 , 40*2)]
dA = [] # длинны отрезка а
for a1,a2 in combinations(Ox,2):
    if all(f(x) == 1 for x in Ox):
        print(a2,a1)
        dA.append(a2 - a1)
print('\n'.join(str(i) for i in dA))
print(min(dA))
