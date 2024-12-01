'''
F(n) = n, при n ≥ 2020,
F(n) = n + 2 + F(n+3), если  n < 2020.
Чему равно значение выражения F(2012) - F(2023)?

'''
from sys import*
setrecursionlimit(10000)
def F(n):
    if n== 1:
        return 1
    return n + F(n - 1)
print(F(2023) - F(2019))