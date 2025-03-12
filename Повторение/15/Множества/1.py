# 4882
s ='¬(x ∈ A) → (¬(x ∈ P) ∨ ¬(x ∈ Q))'
def f(x):
    return (x not in A) <= ((x not in P) or (x not in Q))


A = set()
P = {1, 2, 3, 4}
Q = {1, 2, 3, 4, 5, 6 }

for x in range(501):
    if f(x) == 0:
        A.add(x)
print(A)
