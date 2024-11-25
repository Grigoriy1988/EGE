# (x < A) ∨ (y < A) ∨ (x + 2y > 50)
def f(x,y):
    return  (x < a) or (y < a) or (x + 2*y > 50)

for a in range(0,100):
    if all(f(x,y)==1 for x in range(0,1000) for y in range(0,1000)):
        print(a)
