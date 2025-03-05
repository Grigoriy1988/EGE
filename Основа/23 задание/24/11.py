from functools import*
@lru_cache(None)
def f(c, e, count=0):
    if c %2!=0:
        count+=1
    if c == e and count==1:
        return 1
    if c == e and count!=1:
        return 0
    if c >e:
        return 0
    if c < e:
        return f(c+1,e,count)+f(c+2,e,count)+f(c*2,e,count)
print(f(2,40))
