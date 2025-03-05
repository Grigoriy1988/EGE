def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})

for i in range(6080068, 6080176+1):
    if not div(i):
        print(i)
