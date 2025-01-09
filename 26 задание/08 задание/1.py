f = open('26_2650.txt')
l, m, n = map(int, f.readline().split())
print(l, m, n)
a = ["1"] * l
for i in range(n):
    st, en = map(int, f.readline().split())
    for j in range(st - 1, st + en  -1):
        a[j] = '0'
a = ''.join(a)
a = a.replace('1', ' ')
a = a.split()
F = True
while F:
    print('!')
    print(len(a))
    d = -1
    for i  in  range(len(a)):
        if m > len(a[i]):
            d = i

            break
    else:
        F = False
    if d != -1:
        a.pop(d)
print(len(a))