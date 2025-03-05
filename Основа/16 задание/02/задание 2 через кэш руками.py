cache = dict()

def F(n):
    if n not in cache:

        if n == 1:
            cache[n] = 1
        else:
            cache[n] = F(n-1) + 3*G(n-1)
    return cache[n]

def G(n):
    if n == 1:
        return 1
    return  F(n-1) - 2*G(n-1)

print(F(50))