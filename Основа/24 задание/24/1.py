s = open('24_9169.txt').readline()
k = l = 0
m = 10 ** 6
for r in range(2, len(s)):

    if s[r-2]+s[r-1]+s[r] == 'BAD' or s[r-2]+s[r-1]+s[r] == 'FAT':
        k += 1
    while k == 3:
        m = min(m, r - l + 1)
        if s[l] + s[l +1] + s[l+2] == 'BAD' or s[l] + s[l +1] + s[l+2] == 'FAT':
            k -= 1
        l += 1


        # print(s[l:l+m])
print(m)
