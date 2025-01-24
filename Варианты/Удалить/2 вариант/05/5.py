def f(a):
    s = []
    while a >0:
        s.append(a % 3)
        a //= 3
    s.sort(reverse=True)
    s.append(max(s))

    return  ''.join(str(i) for i in s)
d = []
for n in range(1,12000):
    if int(f(n),3) < 1200:
        d.append(int(f(n),3))
print(max(d))