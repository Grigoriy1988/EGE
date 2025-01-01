s = open('24_13715.txt').readline()
kAB = l = m = 0
for r in range(1, len(s)):
    if s[r - 1] + s[r] == 'AB':
        kAB += 1
    while kAB > 50:
        if s[l]+s[l+1]=='AB':
            kAB-=1
        l+=1
    if kAB == 50:
        m = max(m,r-l+1)
print(m)
