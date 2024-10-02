def перевод(a):
    n_80 = []
    while a > 0:
        n_80.append(a % 80)
        a //= 80
    n_80.reverse()
    s_even = sum(i for i in n_80 if i%2==0)
    s_odd = sum(i for i in n_80 if i % 2 != 0)
    dig = s_even % 80 if s_even >s_odd else s_odd % 80
    n_80.append(dig)
    return дес(n_80)

def дес(a):
    b = 0
    des = 0
    for i in a:
        des += i*80**b
        b+=1
    return  des



