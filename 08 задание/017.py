from itertools import *
n = 0
for i in product(sorted("ФОКУС"), repeat=5):
    s = ''.join(i)
    n+=1
    if 'Ф' not in  s and s.count('У') == 2:
        print(n,s)