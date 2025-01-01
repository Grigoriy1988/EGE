s = open('24_21.txt').readline()
m = 0
l = 0
for r in range(1,len(s)):
    if s[r-1] == s[r]:
        l = r
    if s[r-1] != s[r]:
        m = max(m,r-l+1)
print(m)

s = open('24_21.txt').readline()
m = [1]* len(s)
for i in range(1,len(s)):
    if s[i] != s[i - 1]:
        m[i] += m[i-1]

print(max(m))
