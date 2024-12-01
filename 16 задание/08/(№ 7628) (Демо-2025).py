'''
F(n) = 1, при n = 1;
F(n) = (n - 1)·F(n - 1) при n > 1.
Чему равно значение выражения (F(2024) + 2·F(2023)) / F(2022)?

'''
from sys import *
setrecursionlimit(10000)
def F(n):
    if n== 1:
        return 1
    return (n - 1)*F(n - 1)
print((F(2024) + 2*F(2023)) / F(2022))