
from itertools import *
step = 0
for i in product('01234567',repeat=4):
    s = ''.join(i)
    if s[0]=='2' or s[0]=='4' or s[0]=='6': # или s[0] in '246'
        if s[0]>=s[1]>=s[2]>=s[3]:
            step+=1
            print(step,s)