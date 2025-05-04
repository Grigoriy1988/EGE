from functools import*
@lru_cache(None)

def f(n):
    if n <=3:
        return n
    if n>3 and n % 2 !=0:
        return 2*n + f(n-2)
    return n**2 +f(n-1)
for i in range(1,10001):
    f(i)
print(f(10000) - f(9995))
print(10000**2 + 2 * 9999 + 2*9997)