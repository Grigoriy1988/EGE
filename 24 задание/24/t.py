s = open('24_9169.txt').readline()
#print(s[:50])
l = m = kOR = 0
for r in range(len(s)):
    if r > 2 and (s[r-2]+s[r-1]+s[r] == 'ORO' or s[r-2]+s[r-1]+s[r] == 'ROR'):
        kOR = 0
        l = r - 1
    if r>1 and s[r-1]+s[r] == "RO":
        kOR +=1
    while kOR > 21:
        if s[l] + s[l+1] == 'RO':
            kOR -= 1
        l += 1
    if kOR == 21:
        m = max(m,r-l +1)
print(m)
