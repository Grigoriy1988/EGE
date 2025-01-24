a = [int(i) for i in open('17.txt')]
num = [(a[i], a[i + 1]) for i in range(len(a) - 1) if
       (str(a[i])[-1] == '9' or str(a[i + 1])[-1] == '9') and (a[i] + a[i + 1]) % 2 == 0]
print(len(num), max(sum(i) for i in num))

