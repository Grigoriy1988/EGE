def f(c,e,flag=True):
    if c== 43:
        flag = False
    if c > e:
        return 0
    if c == e:
        return flag
    if c <e:
        return f(c+2,e,flag)+f(c+c-1,e,flag)+f(c+c+1,e,flag)
print(f(7,63))
