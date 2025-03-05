from itertools import *

step = 1
for i in product('БЕРКЛИЙ', repeat=4):
    s = ''.join(i)
    if s[0]!= 'Й' and (s.count('Е')>=1 or s.count('И')>=1):
        print(step, s)
        step += 1
