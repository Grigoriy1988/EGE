from itertools import *
res = set()
for i in range(1,31):
    for d in product("12",repeat=i):
        s = ''.join(d)
        #print(s)


        while '111' in s or '22' in s:
            s = s.replace('111','2',1)
            s = s.replace('222', '1', 1)
            s = s.replace('221', '1', 1)
            s = s.replace('122', '1', 1)
            s = s.replace('22', '2', 1)
        if s.count('1')  == 5:
            res.add(s)
print(len(res))