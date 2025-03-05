from itertools import *
step = 1
for i in product("КМ",'КУМА','КУМА','КУМА','УА'):
    s = ''.join(i)
    print(step,s)
    step+=1