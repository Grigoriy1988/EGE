def p(x):
    return x >1 and all(x % i != 0 for i in range(2,int(x**0.5)+1))
def div(x):
    return sorted({k for i in range(2,int(x**0.5)+1) if x % i == 0 for k in (i, x//i)})

a= 500000-1
for i in range(a,a -100,-1):
    d = [j for j in div(i) if p(j)]
    # print(i,d)
    if sum(d) !=0 and sum(d) % 10==0:
        print(i,sum(d))
