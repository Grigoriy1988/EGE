def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})

for i in range(25317,51237+1):
    d = [j for j in div(i) if not div(j)]
    if len(d) == 6:
        print(i,max(d))

