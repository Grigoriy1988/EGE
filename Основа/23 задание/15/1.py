s='1234567899'
def f(c,e):
    if c >e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c+1,e) + f(int(''.join(s[int(i)] for i in str(c))),e)

print(f(25,51))