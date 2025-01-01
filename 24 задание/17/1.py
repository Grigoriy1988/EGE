s = open('24_4546.txt').readline()
m = [0] * len(s)
for i in range(2, len(s)):
    if s[i - 2] + s[i] == 'AA' or s[i - 2] + s[i] == 'CC':
        m[i] = m[i - 3] + 1 # единица так как троек
print(max(m))
