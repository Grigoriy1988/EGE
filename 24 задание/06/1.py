s = open('24_1302.txt').readline()
s = s.replace('XZZY','XZZ ZZY')
print(max(len(i) for i in s.split()))



s = open('24_1302.txt').readline()
l = 0
m = 0
for r in range(3,len(s)):
    if s[r-3]+s[r-2]+s[r-1]+s[r] == 'XZZY':
        l = r-2
    if s[r - 3] + s[r - 2] + s[r - 1] + s[r] != 'XZZY':
        m =max(m,r-l+1)
        # if 'XZZY'in s[l:r+1]:
        #     print('XZZY'in s[l:r+1])
print(m)