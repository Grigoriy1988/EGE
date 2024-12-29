def f(c,e,command=''):
    if c > e:
        return 0
    if c==e:
        return 1
    if command=='*':
        return f(c+1,e,'+')+f(c+2,e,'+')
    if command != '*':
        return f(c+1,e,'+')+f(c+2,e,'+')++f(c*2,e,'*')

print(f(1,15))