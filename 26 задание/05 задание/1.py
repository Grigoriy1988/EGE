f = open('26_1257.txt')
n = int(f.readline())
print(n)
a  = [int(i) for i in f]
a.sort()
set_a= set(a) # сказать как это важно
s = []
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i] % 2 != a[j]% 2 and (a[i]+a[j]) in set_a:
            s.append(a[i]+a[j])
print(len(s),max(s))
