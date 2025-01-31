from itertools import *

a = 738_000_000
a14 = []
while a > 0:
    a14.append(a % 14)
    a //= 14

print(len(a14), a14[::-1])  # максимальное количество разрядов и само число
# на первом месте не может стоять ни чего кроме 1,2,3,4,5,6 (если взять 7 то следующие два разряда будут 0)
print(6 * 13 * 12 * 11* 10 *9 * 8 * 7)

# Вариант перебор, очень плохой способ
res = set()
for i in permutations('0123456789abcd', 8):
    if i[0] in '089abcd':
        continue
    else:

        dig = int(''.join(j for j in i), 14)
        if dig <= 738_000_000:
            # print(i)
            res.add(dig)
print(len(res))

