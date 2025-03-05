from itertools import *

step = 1
for i in product('ЗЕРКАЛО', repeat=6):
    s = ''.join(i)
    if s.count('К')==1 and s.count('А')==3:
        print(step, s)
        step += 1
