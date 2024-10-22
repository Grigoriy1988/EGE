from itertools import *

step = 1
for i in product('ЖИРАФ', repeat=5):
    s = ''.join(i)
    if s[0]!= 'Ф' and s.count('Ж')==1 and  s[-1]!="Р":
        print(step, s)
        step += 1
