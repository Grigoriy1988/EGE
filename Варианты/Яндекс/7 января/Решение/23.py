def f(c,e):
    if c < e:
        return 0
    if c == e:
        return 1
    if c > e:
        return f(c - int(str(c**2)[0]),e) + f(c - sum(int(i) for i in str(c)),e)

print(f(32,1))