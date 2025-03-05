dig = '0123456789'
s = open('24_1040.txt').readline()
l = 0
m = 0
for r in range(len(s)):
    if s[r] not in dig:
        l = r + 1
    if s[r] in dig:
        m= max(m,r-l+1)
print(m)

