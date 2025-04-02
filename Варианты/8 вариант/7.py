a =1600
b = 1200
i= 10
I = 3
Iисходное = I*1.2
print(Iисходное)
for c in range(1,10):
    V = (a*b*(10+c))/(8*1024*1024)
    if V <= Iисходное:
        print(c)
