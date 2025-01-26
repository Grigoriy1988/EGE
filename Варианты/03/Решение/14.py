def f(a):
    a6 = ''
    while a > 0:
        a6+= str(a % 5)
        a //= 5

    return a6.count('0')

for x in range(2042, 0, -1):
    b = 25 ** 61 + 5 ** 178 - x
    if f(b) == 60:
        print(x)
        break
else:
    print(x)
