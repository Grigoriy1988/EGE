from itertools import *

a = 855_000_000
a15 = []
while a > 0:
    a15.append(a % 15)
    a //= 15

print(len(a15), a15[::-1])  # максимальное количество разрядов и само число
8 [5, 0, 0, 13, 13, 5, 0, 0]
print(4 * 14 * 13 * 12 * 11 * 10 * 9 * 8) # ответ
# Вариант перебор, очень плохой способ
res = set()
for i in permutations('0123456789abcde', 8):
    if i[0] in '06789abcde':
        continue
    else:

        dig = int(''.join(j for j in i), 15)
        if dig <= 855_000_000:
            # print(i)
            res.add(dig)
print(len(res))