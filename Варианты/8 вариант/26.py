f = open('26.txt')
N = int(f.readline())
print(N)
t = [int(i) for i in f]
t.sort()
print(t)
s = 0
count = 0
for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            if a + b <= c:
                break
            else:
                count += 1
                s = max(s, a + b + c)
print(count,s)