f = open('26_936.txt')
N, S = map(int, f.readline().split())
print(N,S)
a = [int(i) for  i in f]
a.sort(reverse=True)
korabl = []
while sum(a) > 0:
    massa = 0
    for i in range(N):
        if a[i]!= 0 and massa + a[i]<=S:
            massa += a[i]
            a[i] = 0

    korabl.append(massa)
print(len(korabl),korabl[-1])