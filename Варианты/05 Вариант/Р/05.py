def f(n):
    a = bin(n)[2:]
    s =sum(int(i) for i in a)
    if s% 2 ==0:
        a = a +'11'
    else:
        a = a + '01'
    return int(a,2)
for n in range(1,100):
    if f(n)>61:
        print(f(n))