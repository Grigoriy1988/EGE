s = open('24_6734.txt').readline()
k = l = 0
m = 10**6
for r in range(0, len(s)):
    if s[r] == '.':
        k += 1
    while k == 7:
        if s[l] == '.':
            k -= 1
        l += 1
        if k == 7:
            m = min(m, r - l + 1)
        # print(s[l:l+m])
print(m)
