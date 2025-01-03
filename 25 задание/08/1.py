def div(x): return sorted({k for i in range(1,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})

for i in range(190201, 190260+1):
    d = [j for j in div(i) if j % 2 == 0]
    if len(d)==4:
        print(i,*d[2:])
