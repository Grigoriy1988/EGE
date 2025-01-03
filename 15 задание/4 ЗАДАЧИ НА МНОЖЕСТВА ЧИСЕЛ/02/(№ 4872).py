#((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))
def f(x):
    return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))

P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
A = set(range(1,1000))


for x in range(1,1000):
    if f(x) == 0:
        A.remove(x)
print(len(A), A)