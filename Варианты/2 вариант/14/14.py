for x in range(401, 10000000):
    n = 16 ** 560 + 16 ** 120 - x
    n16= hex(n)[2:]
    if n16.count('0')==442:
        print(x)
        break
