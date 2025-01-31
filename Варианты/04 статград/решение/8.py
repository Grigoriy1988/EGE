from itertools import *

a = 855_000_000
a15 = []
while a > 0:
    a15.append(a % 15)
    a //= 15

print(len(a15), a15[::-1])  # максимальное количество разрядов и само число
print(4 * 14 * 13 * 12 * 11 * 10 * 9 * 8) # ответ




# Вариант перебор, очень плохой способ
res = set()
for i in permutations('012345689abcde', 8):
    if i[0] in '0689abcde' or (i[0] == '5' and i[1] in '12345689abcde' and i[2] in '12345689abcde'):
        continue
    else:
        dig = int(''.join(j for j in i), 15)
        if dig <= 855_000_000:
            # print(i)
            res.add(dig)
print(len(res))
