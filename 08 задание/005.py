from itertools import *

step = 1
for i in product('КРОТ', repeat=6):
    s = ''.join(i)
    if s.count('О')==1:
        print(step, s)
        step += 1
