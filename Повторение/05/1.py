# (№ 7915) (ЕГКР-2024)
s = '012'
def f(n):
    n3 = []
    while n > 0:
        n3.append(s[n % 3])
        n //= 3
    n3.reverse()
    # print(n3)
    return n3

def R(n):
    r = f(n)
    if n % 3 == 0:
        r.extend(r[-2:])
    else:
        s = sum(int(i) for i in r)
        r.extend(f(s))
    return int(''.join(r),3)

# print(R(11))
for i in range(1,102):
    if R(i) > 220 and R(i) % 2 == 0:
        print(R(i))
        break