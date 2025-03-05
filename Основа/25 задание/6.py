from dee import div
a = 500_001
count = 0
while count < 5:
    d = div(a)[1:-1]
    f = [i for i in d if i!=8 and i%10==8]
    if f:
        print(f'{a} {f[0]}')
        count +=1
    a+=1
