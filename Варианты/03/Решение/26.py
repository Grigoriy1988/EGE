f = open('26.txt')
N, S = map(int, f.readline().split())
print(N, S)
d = {} # словарь для хранения
for i in range(N):
    id_1, length, width, height, massa = map(int, f.readline().split())
    s = length + width + height
    if s in d:
        d[s] +=[id_1]
    else:
        d[s] = [id_1]
for i in sorted(d.keys(), reverse=True):
    if S - len(d[i]) >= 0:
        max_id = max(d[i])
        S -= len(d[i])
        print(d[i], S)
    else:
        print(max_id,len(d[i]))
        break

