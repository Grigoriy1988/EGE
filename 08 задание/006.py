from itertools import *

step = 1
for i in product('КАНТ', repeat=6):
    s = ''.join(i)
    if s.count('К')==2:
        print(step, s)
        step += 1
