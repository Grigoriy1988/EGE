#Перестановки
from itertools import *
step = 0
for i in permutations("КОЛУН",5):
    s=''.join(i)
    s = s.replace('К',"*").replace('Л','*').replace('Н','*')
    s= s.replace('О',"+").replace('У',"+")
    if  '++' not in s and '**' not in s:
        step +=1
        print(step,s)