def f(c, e, t=True):
    if c > e:
        return 0
    if c == 22:
        t = False
    if c == e:
        return t
    if c < e:
        return f(c + 3, e, t) + f(c + 4, e, t)


print(f(16, 38))
