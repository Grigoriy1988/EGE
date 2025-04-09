from fnmatch import *
for x in range(0,10**10+1,999):
    if fnmatch(str(x),'13???57?9'):
        print(x,x//999)