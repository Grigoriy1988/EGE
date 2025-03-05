from itertools import combinations

#(x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not(A)))<=(not P))

Ox  = [i/4  for i in range(14*4,66*4)]
dx = [] # длинны отрезка а
for a1,a2 in combinations(Ox,2):
    # print(a1,a2)
    if all(f(x) == 1 for x in Ox):
        # print(a2-a1)
        dx.append(a2 - a1)
print('\n'.join(str(i) for i in dx))
print(min(dx))

