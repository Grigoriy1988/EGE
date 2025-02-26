f = open('26.txt')
n, v = map(int, f.readline().split())
v *= 1000
print(n, v)
a = sorted([int(i) for i in f if 7000 <= int(i) <= 12000], reverse=True)
print(a)
m = []

while len(a) > 0:
    if sum(m) + a[0] <= v:
        m.append(a[0])
        a.pop(0)
    else:
        a.pop(0)
print(sum(m))
print(len(m), min(m))
