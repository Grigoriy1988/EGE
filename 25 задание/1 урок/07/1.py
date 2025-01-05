def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})
a = 400000000 +1
for i in range(a,a+100000):
    d = div(i)
    if len(d)> 5:
        P = 1
        for j in range(0,5):
            P *= d[j]
    else:
        P = 0
    if P < i and P % 100 == 17:
        print(P,d[4])

