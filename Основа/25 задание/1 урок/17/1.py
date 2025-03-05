def div(x):
    return sorted({k for i in range(2,int(x**0.5)+1) if x % i == 0 for k in (i, x//i)})


for i in range(106732567, 152673836 + 1):
    if int(i**0.5)==i**0.5:
        d = div(i)
        if len(d)==3:
            print(i, max(d))
