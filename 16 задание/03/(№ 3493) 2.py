from functools import*
import sys
sys.setrecursionlimit(1000000000)

@lru_cache(None)
def F(n):
    if n < -100000:
        return 1
    if n > 10:
        return  F(n-1) + 3*F(n-3) + 2
    return -1* F(n-1)


print(F(20))