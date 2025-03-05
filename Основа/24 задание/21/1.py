s = open('24_12476.txt').readline()
kRO = l = m = 0
for r in range(1, len(s)):
    if r > 2 and (s[r - 2] + s[r - 1] + s[r] == "ROR" or s[r - 2] + s[r - 1] + s[r] == "ORO"):
        kRO = 0
        l = r - 1

    if s[r - 1] + s[r] == 'RO':
        kRO += 1
    while kRO > 21:
        if s[l] + s[l + 1] == 'RO':
            kRO -= 1
        l += 1
    if kRO == 21:
        m = max(m, r - l + 1)
        # print(s[l:l+m])
print(m)
