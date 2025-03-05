'''
F(n) = 1, если n < 3
F(n) = F(n – 2) - F(n – 1), если n > 2 и число n чётное,
F(n) = F(n – 2) - F(n – 3), если n > 2 и число n нечётное.



'''


def F(n):
    if n < 3:
        return 1
    if n % 2 == 0:
        return F(n - 2) - F(n - 1)
    return F(n - 2) - F(n - 3)


print(F(50))
