from fnmatch import *
a = 700000 + 1
c = 5
for i in range(a,a+1000000):
    if not fnmatch(str(i),'*0??3*') and not fnmatch(str(i),'*4??2')  and not fnmatch(str(i),'*1*') and i % 13 ==0:
        print(i,sum(int(j) for j in str(i)))
        c -= 1
    if c ==0:
        break