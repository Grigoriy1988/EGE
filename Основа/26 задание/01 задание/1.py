f = open('26_813.txt')
S, N = map(int, f.readline().split())
print(S, N)
a = [int(i) for i in f]
a.sort(reverse=1)
k = 0
sice = 0
while a:
    if a[0] <= S:
        k+=1
        S -= a[0]
        sice = a[0]
        a.pop(0)
    else:
        a.pop(0)
    if a[-1] <= S:
        k += 1
        S -= a[-1]
        a.pop(-1)
        sice = a[0]
    else:
        a.pop(-1)
print(k,sice)
