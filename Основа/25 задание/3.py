from dee import div

for i in range(244143, 367821 + 1):
    # нечетное количество делителей у квадратов
    if int((i ** 0.5)) ** 2 == i:
        if len(div(i)) == 5:
            print(f'{i}: {div(i)[3]}, {div(i)[4]}')
