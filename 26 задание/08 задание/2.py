f = open('26_2650.txt')
l, m, n = map(int, f.readline().split())
print(l, m, n)
a = [0] * (l+1)
for i in range(n):
    st, t = map(int, f.readline().split())
    a[st] += 1
    a[st + t] -= 1
k= 0
st, en = 0,0
count = 0
maxt = 0
for i in range(l+1):
    k0 = k
    k += a[i]
    if k == 0 and st == 0:
        st = i
    if (k == 1 and k0 == 0) or i == l:
        en = i
        t= en - st
        if t >= m:
            count +=1
            maxt = max(t,maxt)
        st,en = 0,0


print(count,maxt)


