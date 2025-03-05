s = open('24_1975.txt').readline()
l = 0
m = 0

for r in range(1,len(s)):
    if s[r-1] + s[r] == 'PP':
       l = r
    if s[r-1] + s[r] != 'PP':
        m  = max(m,r-l +1)
print(m)