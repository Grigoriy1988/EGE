from functools import*
@lru_cache(None)
def f(n):
    if n == 41:
        return 41
    if n % 2 == 0:
        return f(n-1) - n
    return n*f(n-2)

for i in range(41, 9095):
    f(i)
print(f(9094) // f(9089))
