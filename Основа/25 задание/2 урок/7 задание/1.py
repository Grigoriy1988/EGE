from fnmatch import *
def div(x):
    return sum({k for i in range(1,int(x**0.5)+1) if x % i == 0 for k in (i,x//i)})
for i in range(9995597,10**7):
    if fnmatch(str(i),'9?*55*7'):
        print(i,div(i)%21)
