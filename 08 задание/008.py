from itertools import *

step = 1
for i in product('ЛЕТО', repeat=4):
    s = ''.join(i)
    if s.count('Е')>=1:
        print(step, s)
        step += 1
