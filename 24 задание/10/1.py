s = open('24_8510.txt').readline()
s = s.replace('N',"P").replace("O","P")
l=0
m = 0
for r in range(1, len(s)):
    if s[r-1]+s[r]=='PP':
        l = r
    if s[r-1]+s[r]!='PP':
        m = max(m,r-l+1)
print(m)


s = open('24_8510.txt').readline()
s = s.replace('N',"P").replace("O","P")
while 'PP' in s:  s = s.replace('PP', "P P")
print(max(len(i) for i in s.split()))