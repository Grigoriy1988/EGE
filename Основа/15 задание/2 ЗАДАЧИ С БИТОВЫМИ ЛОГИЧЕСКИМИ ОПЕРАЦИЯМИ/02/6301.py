#(X & 123 ≠ 0 ∨ X & 98 ≠ 0) → (X & 75 = 0 → X & А ≠ 0)
def f(x):
    return ((x & 123  != 0) or (x & 98 != 0)) <= ((x & 75 == 0) <= (x & a != 0))

for  a in range(1,1000):
    if all(f(x)==1 for x in range(1,100000)):
        print(a)
