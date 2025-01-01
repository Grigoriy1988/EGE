s = open('24_10105.txt').readline()
l = 0
m = 0
kT = 0
for r in range(len(s)):
    if s[r] == "T":
        kT += 1

    while kT >= 101:
        if s[l] == "T":
            kT -=1
        l+=1
    if kT == 100:
        m = max(m, r - l + 1)
print(m)