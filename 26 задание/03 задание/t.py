f = open('26_936.txt')
n, s = map(int, f.readline().split())
# print(n,s)
a = [int(i) for i in f]
a.sort(reverse=True)
k = []
while sum(a)>0:
    m = 0
    for i in range(n):
        if a[i] + m <= s and a[i] != 0:
            m += a[i]
            a[i] = 0
    k.append(m)
print(len(k),k[-1])
