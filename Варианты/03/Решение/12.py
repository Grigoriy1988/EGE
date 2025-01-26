def f(a):
    return sum(int(i) for i in a)

for n in range(3,10000):
    s= '0'+"2"*n
    while '002' in s or '22' in s:
        if '002' in s:
            s = s.replace('002','44',1)
        else:
            s = s.replace('22', '0', 1)
        if '222' in s:
            s = s.replace('222','2',1)
    if f(s) == 42:
        print(n,s)


