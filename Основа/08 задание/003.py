from itertools import *
step = 1
for i in product('ABC','ABC','ABC','ABC','ABCX'):
    s = ''.join(i)
    print(step,s)
    step+=1