f = open('26_2480.txt')
n = int(f.readline())
a = ['0'] * 2_000_000
for _ in range(n):
    st, en = map(int, f.readline().split())
    # print(st, en)
    for i in range(st, en):
        a[i] = "1"
a = ''.join(a)
a = a.replace("0", ' ').split()
# print(a[:3])
print(len(a), sum(sum(int(j) for j in a[i]) for i in range(len(a))))

