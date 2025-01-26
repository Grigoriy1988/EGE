f = open('17.txt')
a = [int(i) for i in f]
c = [i for i in a if abs(i) % 2042 == 0]
b = [(a[i], a[i + 1]) for i in range(len(a) - 1) if a[i]+ a[i + 1] > len(c)]
print(len(b), max(sum(i) for i in b))
