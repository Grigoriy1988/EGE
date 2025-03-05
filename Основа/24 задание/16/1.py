s = open('24_9552.txt').readline()
m=[0]*len(s)
for i in range(1,len(s)):
    if s[i-1]+ s[i] == "PC":
        m[i] = m[i-2]+2
    if i>=3 and s[i-3]+s[i-2]+s[i-1]+s[i] == 'CSGO':
        m[i] = m[i-4] + 4

print(max(m))
