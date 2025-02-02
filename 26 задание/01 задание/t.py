f = open('26_813.txt')
s, n = map(int, f.readline().split())
print(s,n)
a = [int(i) for i in f]
a.sort(reverse=1)
# print(a)
k = 0
sice = 0
max_sice = 0
min_sice = 0
while a:
    while max_sice ==0 and len(a)>0:
        if a[0] <= s:
            k += 1
            s -=a[0]
            max_sice = a[0]
            a.pop(0)
        elif len(a) > 0:
            a.pop(0)
    sice = max_sice if max_sice !=0 else sice
    max_sice = 0
    while min_sice == 0 and len(a)>0:
        if len(a)> 0 and a[-1] <= s:
            k += 1
            s -= a[-1]
            min_sice = a[-1]
            a.pop(-1)
        elif len(a)> 0:
            a.pop(-1)
    sice = min_sice if min_sice != 0 else sice
    min_sice = 0
print(k,sice)
