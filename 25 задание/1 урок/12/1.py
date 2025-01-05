def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})
a = 550000 + 1
for i in range(a,a+100):
    d = [j for j in div(i) if j %10 == 7]
    if len(d)==3:
        print(i,max(d))
