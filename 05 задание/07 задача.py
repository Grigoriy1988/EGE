цифры = '0123456789ABCDEF'
def перевод(a, new):
    dig_s = ''
    while a > 0:
        dig_s = цифры[a % new] + dig_s
        a = a // new
    return dig_s

for n in range(1, 1000):
    n_12 = перевод(n, 12)
    print(f'n={n},n_12={n_12}')
    if n%12 ==0:
        n_12=n_12+n_12[-3:]
    else:
        n_12 = перевод(n%12*3,12)+n_12
    print(f'n={n},n_12={n_12}')
    R = int(n_12,12)
    # if R< 58000:
    #     print(f'n={n},n_12={n_12} R = {R}')
