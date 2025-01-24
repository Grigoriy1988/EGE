# ((w→y)→x)∨¬z
from itertools import product
print(f'x\ty\tw\tz\tf')
for x, y, w,z in product([0, 1], repeat=4):
    f = ((w<=y)<=x) or (not z)
    if f ==0:
        print(f'{x}\t{y}\t{w}\t{z}\t{f}')