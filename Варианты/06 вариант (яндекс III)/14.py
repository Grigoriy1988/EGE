def f(a):
    s = ''
    while a > 0:
        s =  str(a % 9) + s
        a //=9

    return s.count('0')
m = 0
for x in range(0,1951):
    b = 72070 + 7400 - x
    m = max(m,f(b))
print(m)
