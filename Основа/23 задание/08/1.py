def f(c,e,f1=False,f2=False):
    if c==9:
        f1 = True
    if c==12:
        f2 = True
    if c > e:
        return 0
    if c == e:
        return f1*f2
    if c <e:
        return f(c+1,e,f1,f2)+f(c+3,e,f1,f2)+f(c*2,e,f1,f2)
print(f(3,20))