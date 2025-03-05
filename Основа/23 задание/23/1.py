from functools import*
@lru_cache(None)
def f(c, e, command=''):
    if c > e:
        return 0
    if c == e and command.count('*') <= 3 :
        return 1
    if c == e and command.count('*') > 3 :
        return 0
    return f(c + 2, e, command + '+') + f(c * 3, e, command + '*') + f(c * 5, e, command + '*')

print(f(2,200))
