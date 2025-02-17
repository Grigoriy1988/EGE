def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b[:3] + b
    else:
        b =  b + bin(((n % 5) * 5))[2:]
    return int(b,2)
for i in range(1,10002,2):
    if f(i)<313:
        print(i)
