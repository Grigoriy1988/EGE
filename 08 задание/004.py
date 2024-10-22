from itertools import *
step = 1
for i in product('ЭЮЯ','АБВГ','АБВГ','АБВГ','ЭЮЯ'):
    s = ''.join(i)
    print(step,s)
    step+=1