num = 6 ** 1333 - 5 * 6 ** 1215 + 3 * 6 ** 144 - 86
num_6 = []
while num > 0:
    num_6.append(num % 6)
    num //= 6

print(sum(num_6))