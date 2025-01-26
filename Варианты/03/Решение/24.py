f = open('24.txt').readline()
f = f.replace('*', '+')
print(f[:20])
f = f.split('+')
print(f[:20])

l = 0
m = max_len = 0
for r in f:
    if r != '' and r[0]!= 0:
        m += 2
        max_len = max(max_len,m)
    else:
        m =0
print(max_len)