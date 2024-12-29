# from functools import*
# @lru_cache(None)
def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    return f(c+2,e)+f(c+4,e)+f(c+5,e)

for i in range(31,100):
    if f(31,i) == 1001:
        print(i)
        break