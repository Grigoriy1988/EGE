s = open('24_2427.txt').readline()
lower_line = ''
line = ''
l = 0
for r in range(1, len(s)):
    if s[r] < s[r - 1]:
        line = s[l:r + 1]
        if len(line) > len(lower_line):
            lower_line = line
    else:
        l = r
print(lower_line)

s = open('24_2427.txt').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        m[i] += m[i - 1]
mx = max(m)
for i in range(1, len(s)):
    if m[i] == mx:
        print(s[i - mx + 1:i + 1])
