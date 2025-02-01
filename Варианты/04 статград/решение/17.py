f = open('17.txt')
a = [int(i) for i in f]
b = min(a) % 5
c = max(a) % 7
triad = [(a[i], a[i + 1], a[i + 2]) for i in range(len(a) - 2) if
         any(len(str(j)) == 4 for j in (a[i], a[i + 1], a[i + 2])) and [a[i] % 5, a[i + 1] % 5, a[i + 2] % 5].count(
             b) <= 1 and [a[i] % 7, a[i + 1] % 7, a[i + 2] % 7].count(c) >= 2]
print(len(triad), max(sum(x) for x in triad))


