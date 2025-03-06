dig = '0123456789abcdefghi'
def f(n):
    n19 = []
    while n >0:
        n19 = [dig[n % 19]] + n19
        n //= 19
    return n19

def R(n):
    n19 = ''.join(f(n))
    # print(n19)
    for i in 'bcdfgh':
        # print(i)
        n19 =n19.replace(i,'5')
    # print(n19)
    n19 = ''.join(f(n % 19)) + n19
    n19 = n19[-2:] + n19[:-2]
    for i in 'bcdfgh':
        # print(i)
        n19 =n19.replace(i,'5')
    # print(n19)
    n19 = ''.join(f(n % 19)) + n19
    n19 = n19[-2:] + n19[:-2]
    return int(n19,19)
m = []
for n in range(100_000,1_000_000):
    if sum(int(i) for i in str(R(n))) % 7 == 0:
        m.append(R(n))
print(max(m))