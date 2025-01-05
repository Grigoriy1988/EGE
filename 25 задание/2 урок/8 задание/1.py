from fnmatch import *
def div(x):
    return sum({k for i in range(1,int(x**0.5)+1) if x % i == 0 for k in (i,x//i)})
for i in range(0,10**7,8*7*3):
    if fnmatch(str(i),'?6*6*?6'):
        print(i,div(i))

