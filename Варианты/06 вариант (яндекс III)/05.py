def f(a):
    r = bin(a)[2:]
    r = r + str( sum(int(i) for i in r) % 2)
    r = r + str(sum(int(i) for i in r) % 2)
    return int(r,2)
for n in range(200):
    if f(n)>198:
        print(f'{n} -> {f(n)}')
