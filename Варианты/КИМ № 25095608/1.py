a, b, c, d = map(int, input('Введите четыре числа: ').split())
if a >= b and a >= c and a >= d:
    print('Наибольшее число ', a)
elif b >= a and b >= c and b >= d:
    print('Наибольшее число ', b)
elif c >= a and c >= b and c >= d:
    print('Наибольшее число ', c)
else:
    print('Наибольшее число ', d)
