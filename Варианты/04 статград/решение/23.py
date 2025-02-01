def f(c, e, flag=True):
    if c == 16:
        flag = False
    if c < e:
        return 0
    if c == e:
        return flag
    if c > e:
        return f(c - 2, e, flag) + f(c // 3 if c % 3 == 0 else c - 4, e, flag)


print(f(36, 4))

