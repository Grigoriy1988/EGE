def f(c,e,flag=False):
    if c==43:
        flag=True
    if c<e:
        return 0
    if c==e:
        return flag
    if c>e:
        return f(c-8,e,flag)+f(c//2,e,flag)
print(f(102,5))