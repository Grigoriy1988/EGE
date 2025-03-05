def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})
a = 300000 + 1
for i in range(a,a+1000):
    d = [j for j in div(i) if j % 3 == 0]
    if len(d)==5:
        print(i,max(d))
