def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})

for i in range(1204300, 1204380+1):
    d = [j for j in div(i) if j % 2 == 0]
    s = sum(d) if d else 0
    if s >0 and s%10==0:
        print(i,s)
