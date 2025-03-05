from itertools import *
k = 1
for i in product(sorted('ФОКУС'), repeat=5):
    s = ''.join(i)
    # print(k,s)

    if 'Ф' not in s and s.count('У')==2:
        print(k,s)
    k += 1