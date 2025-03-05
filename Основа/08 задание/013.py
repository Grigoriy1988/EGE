#Перестановки
from itertools import *
step = 0
for i in permutations("ПЕСКАРЬ",7):
    s=''.join(i)
    if  s[0]!= 'Ь' and 'ЬЕ' not in s and 'ЬА' not in s and 'ЬР' not in s:
        step +=1
        print(step,s)