from itertools import *
n = 0
for i in product(sorted("ИЮНЬ"), repeat=5):
    n +=1
    s = ''.join(i)
    if s.count('И')+s.count('Ю')==2:
        print(n,s)