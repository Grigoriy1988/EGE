def f(a):
    even_number = []
    odd_number = []
    s = str(a)
    for i in s:
        if int(i) % 2 == 0:
            even_number.append(int(i))
        else:
            odd_number.append(int(i))
    return even_number, odd_number


count = 0
for n in range(1000, 10000):
    if len(f(n)[0]) != 0 and len(f(n)[1]) != 0:
        s = sum(f(n)[0]) if len(f(n)[0]) >= len(f(n)[1]) else sum(f(n)[1])
        R = str(s) + str(max(f(n)[0])) if s % 2 == 0 else str(min(f(n)[1])) + str(s)
        # print(f'n={n} R={R}')
        if int(R) == 111:
            count += 1
print(count)
