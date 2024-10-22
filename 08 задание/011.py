#Перестановки
from itertools import *
step = 0
for i in permutations("КАЛИЙ",5):
    s=''.join(i)
    if s[0] != 'Й' and 'ИА' not in s:
        step +=1
        print(step,s)