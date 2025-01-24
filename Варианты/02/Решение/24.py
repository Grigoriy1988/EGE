f = open('24.txt').readline()
r = 0
m = 0
mp = 0
while r <= len(f) - 2:
    if f[r] + f[r+1] == 'AN' or f[r] + f[r+1] == 'AE':
        mp +=1
        r +=2
    else:
        m = max(mp,m)
        r+=1
        mp = 0
print(m)