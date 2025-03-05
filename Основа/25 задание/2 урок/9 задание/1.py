from fnmatch import *
def div(x):
    return {k for i in range(1,int(x**0.5)+1) if x % i == 0 for k in (i,x//i)}
for i in range(0,10**7+1,217):
    if fnmatch(str(i),'14?4*'):
        print(i,sum(j for j in div(i) if j% 2!=0))


