num = 15 + 2 ** 10 + 16
num_16 = []
while num > 0:
    num_16.append(num % 16)
    num //= 16

print(num_16.count(15))
print(num_16[::-1])

dig = '0123456789ABCDEF'
num = 15 + 2 ** 10 + 16
num_16 = []
while num > 0:
    num_16.append(dig[num % 16])
    num //= 16

print(num_16.count('F'))
print(''.join(x for x in num_16[::-1]))
