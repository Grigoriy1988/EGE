def p(x):
    return x >1 and all(x % i != 0 for i in range(2,int(x**0.5)+1))

def div(x):
    return sorted({k for i in range(1,int(x**0.5)+1) if x % i == 0 for k in (i, x//i)})


for i in range(113_000_000, 114_000_000 + 1):
    if i % 2 == 0 and i %4 !=0:
        t= i // 2
        if t == int(t**0.5)**2 and p(int(t**0.5)):
            print(i,2*int(t**0.5))


