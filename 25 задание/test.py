def div(a):
    return sorted({k for i in range(2, int(a ** 0.5) + 1) if a % i == 0 for k in (i, a // i)})
def p(x):
    return x > 1 and all( x % i !=0 for i in range(2, int(x ** 0.5) + 1) )

b = 500000 - 1
for i in range(b, b - 100,-1):
    d = [j for j in div(i) if p(j)]
    if sum(d) != 0 and sum(d)% 10 == 0:
        print(i,sum(d))
