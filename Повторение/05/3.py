dig = '0123456789abcdefghij'
def f(n):
    n19=[]
    while n >0:
        n19 = [dig[n % 19]] + n19
        n //= 19
    return n19
def r(n):
    n19= ''.join(f(n))
    for i in 'ВCDFGH'.lower():
        n19 = n19.replace(i,'5')
    n19 = ''.join(f(n %19)) + n19
    n19 = n19[-2:] + n19[:-2]

    for i in 'ВCDFGH'.lower():
        n19 = n19.replace(i,'5')
    n19 = ''.join(f(n %19)) + n19
    n19 = n19[-2:] + n19[:-2]
    return int(n19,19)


print(f(18))
m = []
for n in range(100_000,1_000_000):
    if sum(int(i) for i in str(r(n))) % 7 == 0:
        m.append(r(n))
print(max(m))



