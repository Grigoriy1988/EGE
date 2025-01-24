s = open('24.txt').readline()
l = 0
m = 0
mABA = 0
r = 3
while r + 3 <= len(s):
    if s[r-2]+s[r-1]+s[r] =='ABA' or s[r-2]+s[r-1]+s[r] =='BAB':
        r += 3
        m += 1
    elif s[r - 2] + s[r - 1] + s[r] != 'ABA' or s[r - 2] + s[r - 1] + s[r] != 'BAB':
        mABA = max(m,mABA)
        m = 0
        r+=1
print(mABA)
