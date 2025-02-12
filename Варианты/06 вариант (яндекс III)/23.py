# from functools import*
# @lru_cache(None)
def f(c, e, t1=False, t2=True):
    if c == 33:
        t1 = True
    if c == 35:
        t2 = False
    if c > e:
        return 0
    if c == e:
        return int(t1 and t2)
    return f(c + 1, e, t1, t2) + f(c + 2, e, t1, t2) + f(c + 4, e, t1, t2)


print(f(24, 42))
