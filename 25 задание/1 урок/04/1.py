def div(x):
    return sorted({k for i in range(2,int(x**0.5)+1) if x % i == 0 for k in (i, x // i) })

a = 150001
count = 0
while count <7:
    d = div(a)
    S  = 0 if len(d) == 0 else sum(d)
    if S % 13 == 10:
        print(a,S)
        count +=1
    a += 1
