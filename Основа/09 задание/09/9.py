file = open('input.txt', mode='r')
count = 0
for string in file:
    a = [int(i) for i in string.split()]
    a_1  = [i for i in a if i % 2 == 0]
    f = a[0] + a[1] != a[2] + a[3] and a[0] + a[2] != a[1] + a[3] and a[0] + a[3] != a[1] + a[2]
    if a_1:
        if (max(a_1) < sum(a) - max(a_1)) and  f:
            count += 1



print(count)
