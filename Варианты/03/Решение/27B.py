def contiguous(k1, k2):
    x1, y1 = k1
    x2, y2 = k2
    return int((x1 == x2) and abs(y1 - y2 == 1) or (y1 == y2) and abs(x1 - x2 == 1))


def sociality(x):
    global animals
    res = 0
    for a in x:
        count = 0
        for b in animals:
            if a == b: continue
            r = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
            if r <= 0.1:
                count += 1
            if count >= 14:
                res += 1
                break
    return res


animals = [list(map(float, i.split())) for i in open('27_B.txt')]
# print(animals)
cluster = {}
for x, y in animals:
    a, b = int(x), int(y)
    if (a, b) in cluster:
        cluster[(a, b)] += [[x, y]]
    else:
        cluster[(a, b)] = [[x, y]]
# for a,b in cluster:
#     print(cluster[(a,b)])

max_count = []
for i in cluster:
    for j in cluster:
        for p in cluster:
            if contiguous(i, j) + contiguous(i, p) + contiguous(j, p) >= 2 and len(set((i, j,p))) == 3:
                s = cluster[i] + cluster[j] + cluster[p]
                if len(s) > len(max_count):
                    max_count = s
print(len(max_count))
print(sociality(max_count))
print(len(max_count) - sociality(max_count))
