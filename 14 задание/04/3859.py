for x in range(100000000):
    num = 64**12 - 8**14 + x
    num_8 = []
    while num > 0:
        num_8.append(num % 8)
        num //= 8
    if num_8.count(7) == 12 and num_8.count(1) == 1:
        print(x)
        break