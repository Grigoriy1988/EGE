#Перестановки
from itertools import *
step = 0
set_s = set()
for i in permutations("АССАСИН",7):
    s=''.join(i)
    step +=1
    set_s.add(s)
    print(step,s)
print(len(set_s))

#"либо for i in set(permutations("АССАСИН",7)):"
