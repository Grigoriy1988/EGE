num = 7**2103 - 6*7**1270 + 3*7**57 - 98
num_7 = []
while num > 0:
    num_7.append(num % 7)
    num //= 7

print(sum(num_7))
print(num_7.count(1))
print(num_7[::-1])