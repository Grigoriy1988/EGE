s = open('24_2251.txt').readline()
l = 0
m = 0
kD = 0
for r in range(len(s)):
    if s[r] == "D":
        kD += 1
    while kD >= 3:
        if s[l] == "D":
            kD -=1
        l +=1
    m = max(m, r - l +1)
print(m)

