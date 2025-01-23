f = open('26.txt')
L, P, N = map(int, f.readline().split())
stavki = []
for i in range(L):
    stavki.append([0])

for i in range(N):
    l_num, num_u,stavka = map(int, f.readline().split())
    stavki[l_num-1].append(stavka)
    # print(stavki)
count =0
itog = 0
print(stavki)
for i in range(len(stavki)):
    a = sorted([x for x in stavki[i] if x >0])
    # print(a)
    if len(a) >= 2:
        count +=1
        itog += a[-2]

print(count,itog)