file = open('9.txt', mode='r')
count = 0
for string in file:
    a = sum(sorted([int(x) for x in string.split()])[1:4]) / 3
    if a >= 8:
        count += 1
print(count)
