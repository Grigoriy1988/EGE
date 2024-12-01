'''
F(n)=G(n) = 1 при n =1
F(n)= F(n-1) + 3G(n-1) при n>1
G(n) = F(n-1) – 2G(n-1) при n>1

'''
def F(n):
    if n == 1:
        return 1
    return  F(n-1) + 3*G(n-1)
def G(n):
    if n == 1:
        return 1
    return  F(n-1) - 2*G(n-1)

print(F(50))