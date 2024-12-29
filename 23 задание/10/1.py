def f(c,e,f1=False,f2=True):
    if c == 25:
        f1 = True
    if c == 6:
        f2=False
    if c > e:
        return 0
    if c == e:
        return f1*f2
    if c<e:
        return f(c+2,e,f1,f2)+f(c*3,e,f1,f2)
print(f(1,63))