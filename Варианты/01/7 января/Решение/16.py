from functools import *


# from sys import*
# setrecursionlimit(100000)
@lru_cache(None)
def f(n):
    if n >= 2024:
        return 1
    else:
        return f(n + 2) + f(n + 4)


# for i in range(2024, 0, -1):
#     f(i)

a = set()
for i in range(3000, 0, -1):
    a.add(f(i))
print(len(a))
