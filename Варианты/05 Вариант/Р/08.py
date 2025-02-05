from itertools import*
# product - перестановки
n = 1
for i in product(sorted("СЕНТЯБРЬ"), repeat=5):
    s = ''.join(lit for lit in i)
    if n% 2 == 0 and s[0]=="Р" and "Ь" not in s:
        print(f'{n}){s}')
    n+=1