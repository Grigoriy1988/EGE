def f (c,e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c< e:
        return f(c+3,e)+ f(c*2,e) + f(c*3,e)
print(f(1,58))