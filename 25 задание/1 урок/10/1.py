def div(x): return sorted({k for i in range(2,int(x**0.5)+1) if x % i ==0 for k in (i, x// i)})

a = 500_001
count = 0
while count < 5:
    d = div(a)[1:-1]
    f = [i for i in d if i!=8 and i%10==8]
    if f:
        print(f'{a} {f[0]}')
        count +=1
    a+=1