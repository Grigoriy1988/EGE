#(x&5160 > 0 \/ x&3650 > 0) → (x&9545 = 0 → x&А > 0)
def f(x):
    return ((x&5160 > 0) or (x&3650 > 0)) <= ((x&9545 == 0) <= (x & A > 0))

for A in range(1,9545+100):
    if all(f(x) for x in range(1,9545*2)):
        print(A)