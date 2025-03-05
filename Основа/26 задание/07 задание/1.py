f = open('26_2480.txt')
n = int(f.readline())
a = ['0'] * 2_000_000
for i in range(n):
    st, en = map(int, f.readline().split())
    for j in range(st, en):
        a[j] = '1'
a = ''.join(a)
a = a.replace('0',' ')
a = a.split()
s = sum(sum(int(j) for j in a[i] )for i in range(len(a)))
print(len(a),s)
