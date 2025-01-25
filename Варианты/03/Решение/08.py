from itertools import *

n = 0
for i in product(sorted("ПРОБНИК"), repeat=6):
    s = ''.join(i)
    n += 1
    if s.count('О') == 3 and s.count('П') <= 1 and s.count('Р') <= 1 and s.count('Б') <= 1 and s.count(
            'Н') <= 1 and s.count('Н') <= 1 and s.count('И') <= 1 and s.count('К') <= 1:
        print(n, s)

# len(set(s)) == 4
