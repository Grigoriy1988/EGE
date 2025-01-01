s = open('24_2423.txt').readline()
m=[1]*len(s)
for i in range(1,len(s)):
    if s[i] > s[i-1]:
        m[i] += m[i-1]
print(max(m))