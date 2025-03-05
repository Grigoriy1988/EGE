# (х + у ≤ 30) ∨ (у ≤ х+2) ∨ (у ≥ А)
def f(x,y):
    return  (x + y <= 30) or (y <= x +2) or (y >= a)

for a in range(0,100):
    if all(f(x,y)==1 for x in range(0,1000) for y in range(0,1000)):
        print(a)
