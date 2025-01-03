def p(x):
    return x >1 and all(x % i != 0 for i in range(2,int(x**0.5)+1))
def div(x):
    return sorted({k for i in range(2,int(x**0.5)+1) if x % i == 0 for k in (i, x//i)})


for i in range(125697, 125721 + 1):
    d = div(i)
    if len(d)==2 and p(d[0]) and p(d[1]):
        print(*d)

