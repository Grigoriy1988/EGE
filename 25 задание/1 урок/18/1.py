def p(x):
    return x >1 and all(x % i != 0 for i in range(2,int(x**0.5)+1))

def div(x):
    return sorted({k for i in range(1,int(x**0.5)+1) if x % i == 0 for k in (i, x//i)})


for i in range(55_000_000, 60_000_000 + 1):
    t = i
    while t % 2==0:
        t //=2
    if t == int(t**0.25)**4 and p(int(t**0.25)):
        print(i,t)


    # d = [k for k in div(i) if k % 2 !=0]
    # if len(d)==5:
    #     print(i, max(d))

