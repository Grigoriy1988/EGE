from itertools import *
n = 0
for i in permutations("КАБИНЕТ", 7):
    s = ''.join(i)
    if s[-1] not in "АИЕ":
        n += 1
        print(n,s)
