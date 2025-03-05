цифры = '0123456789ABCDEF'


def перевод(a, new):
    dig_s = ''
    while a > 0:
        dig_s = цифры[a % new] + dig_s
        a = a // new
    return dig_s


for n in range(1, 2000):
    n_3 = перевод(n, 3)
    if n % 3 == 0:
        n_3 = "1" + n_3 + "02"
    else:
        n_3 = n_3 + перевод(n % 3 * 4, 3)
    R = int(n_3, 3)
    if R < 199:
        print(f'N={n} троичное {n_3} R = {R}')
