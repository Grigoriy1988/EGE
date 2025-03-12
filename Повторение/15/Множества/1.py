# 8007
s ='(¬(x ∈ A)) → (((x ∈ Q) → (x ∈ P)) → (x ∈ R)) ∨ (x > 500))'
def f(x):
    return (x not in A) <= (((x in Q) <= (x in P)) <= (x in R)) or (x > 500)


A = set()
P = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
Q = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
R = {0, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40}
for x in range(501):
    if f(x) == 0:
        A.add(x)
p = 1
for i in A:
    p*= i
print(p)
for x in range(501):
    if f(x) == 0:
       print(x)
