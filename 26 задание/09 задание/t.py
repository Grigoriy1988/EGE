f  = open('26_2651.txt')
n = int(f.readline())
a = [[0] * 9 for i in range(2025)]
for i in range(n):
    y, t = map(int, f.readline().split())
    a[y][t] +=1
count = 0
year = [0,0]
for i in range(1961,1992):
    k = 0
    for j in range(1,9):
        if a[i][j] == 0:
            k+=1
    count += k
    if k >= year[1]:
        year = [i,k]

print(a[1961:1992])
print(count,year)

