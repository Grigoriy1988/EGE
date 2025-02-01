from functools import *
@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n % 4 < 2:
        return f(n // 4) + n % 4
    return f(n // 4) + n % 4 - 1


for i in range(0, 1000000000):
    if f(i) == 27 and f(i + 1) == 16:
        print(i)


