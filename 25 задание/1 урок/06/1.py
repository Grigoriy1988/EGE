def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})
a = 550000 +1
for i in range(a,a+1000):
    d = div(i)
    F = sum(d) // len(d) if len(d)>0 else 0
    if F !=0 and F % 31  == 13:
        print(i, F)
