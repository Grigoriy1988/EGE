def f (a):
    abin = bin(a)[2:]
    if a % 2 != 0:
        abin = abin[:-2] + '10'
    else:
        abin = '10' + abin[2:] + '1'
    return int(abin,2)
r= set()
for n in range(26,10000):
    r.add(f(n))
    print(min(r))