'''
F(n) = 1, при n < -100000,
F(n) = F(n–1) + 3·F(n–3) + 2, при n > 10,
F(n) = -F(n–1) для остальных случаев.

'''
from functools import*
import sys

@lru_cache(None)
def F(n):
    if n < -100000:
        return 1
    if n > 10:
        return  F(n-1) + 3*F(n-3) + 2
    return -1* F(n-1)

for i in range(-100000,20):
    F(i)
print(F(20))