from functools import *
@lru_cache(None)
def f(c,e,count=0):
    if c%2 == 0:
        count+=1
    if c==e and count==6:
        return 1
    if c==e and count!=6:
        return 0
    if c>e:
        return 0
    return f(c+1,e,count)+f(c+3,e,count)+f(c+5,e,count)
print(f(3,25))