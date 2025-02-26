from fnmatch import *
count = 0
for a in range(2123214525,10**10+1,2025):
    if fnmatch(str(a),'21?3*145?5'):
        print(a,a // 2025)
        count+=1
print(count)