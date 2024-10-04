numbers = '012'


def algorithm(a):
    result = ''
    while a > 0:
        result = numbers[a % 3] + result
        a //= 3
    return result

R_list = []
for N in range(1, 160):
    R = algorithm(N)
    # print(R)
    if N % 5 != 0:
        R = R[:-1] + R[0] + algorithm(N % 5)
    else:
        R = R + R[-1] + R[-1]
    # print(R)
    R = int(R,3)

    if R>123:
        print(f'N={N}, R={R}')
        R_list.append(R)
print(f'Ответ {min(R_list)}')