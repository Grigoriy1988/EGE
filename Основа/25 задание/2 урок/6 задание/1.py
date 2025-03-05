from fnmatch import *
def div(x):
    return {k for i in range(1,int(x**0.5)+1) if x% i == 0 for k in (i,x//i)}
count = 7
for i in range(65001,65001+1000000):
    if fnmatch(str(i),'6*97*5?'):
        d = [j for j in div(i) if j %2==0]
        if len(d) >= 4:
            print(i,sum(d))
            count-=1
    if count==0:
        break