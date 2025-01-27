def f(c,e,a1=False,a2=True):
    if c == e:
        return a1*a2
    if c ==26:
        a1 =True
    if c == 12:
        a2 =False
    if c < e:
        return 0
    if c > e:
        return f(c-2,e,a1,a2) +f(c//2,e,a1,a2)
print(f(42,1))
