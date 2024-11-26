#¬(x ∈ A) → ¬((x ∈ P) ∨ (x ∈ Q))
def f(x):
    return (x not in A) <= (not((x in P) or (x in Q)))

P = { 1, 2, 4, 8 }
Q = { 1, 2, 3, 4, 5, 6 }
A = set()


for x in range(1,1000):
    if f(x) == 0:
        A.add(x)
print(len(A),A)