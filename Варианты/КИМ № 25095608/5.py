def t(n):
    N3 = ''
    while n > 0:
        N3 = str(n % 3) + N3
        n //= 3
    return N3


def f(N):
    N3 = t(N)
    if N % 3 ==0:
        N3 = N3 + N3[-2:]
    else:
        p = t((N%3)*3)
        N3 =N3 +p
    return int(N3,3)
res = []
for i in range(2,10000):
   if f(i) <= 150:
       res.append(i)
print(max(res))