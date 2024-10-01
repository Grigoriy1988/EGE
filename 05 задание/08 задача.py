цифры = '0123456789ABCDEFGHI' #19 cc


def перевод(a, new):
    dig_s = ''
    while a > 0:
        dig_s = цифры[a % new] + dig_s
        a = a // new
    return dig_s
r_max = 0
for n in range(10000, 100000):
    n_19 = перевод(n, 19)
    # print(n_19, end=' ')
    # согласные буквы (В, C, D, F, G, H) заменяются на 5;
    sogl = 'BCDFGH'
    for i in sogl:
        n_19 = n_19.replace(i,'5')
    # print(n_19,end=' ')
    n_19 = перевод(n%19,19)+n_19
    # print(n_19, end=' ')
    n_19 = n_19[-2:] + n_19[:-2]
    # print(n_19)

    #повтор
    for i in sogl:
        n_19 = n_19.replace(i,'5')
    # print(n_19,end=' ')
    # n_19 = перевод(n%19,19)+n_19 спорный момент
    # print(n_19, end=' ')
    n_19 = n_19[-2:] + n_19[:-2]
    # print(n_19)
    r= int(n_19,19)
    s = sum(map(int,str(r)))
    if s%7 ==0:
        r_max = max(r_max,r)
        print(n,r,s)
print(r_max)



