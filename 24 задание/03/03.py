# динамика
s = open('24_1040.txt').readline()
m = [0]*len(s)
for i in range(0,len(s)):
    if s[i] in '0123456789':
        m[i]+=m[i-1]+1

print(max(m))
print(', '.join(i for i in s[:50]))
print(m[:50])