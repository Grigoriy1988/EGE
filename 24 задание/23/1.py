s = open('24_11954.txt').readline()
k = l = 0
m = 10 ** 6
for r in range(0, len(s)):
    if s[r] == 'Y':
        l = r + 1
        k = 0
    if s[r] == 'X':
        k += 1
    while k == 500:
        m = min(m, r - l + 1)
        if s[l] == 'X':
            k -= 1
        l += 1


        # print(s[l:l+m])
print(m)
