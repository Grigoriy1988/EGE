# расстояние
def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

# Центр кластер
def center(cluster):
    summ_dit = []
    for p in cluster:
        sm = sum(dist(p,p1) for p1 in cluster)
        summ_dit.append([sm,p])
    return min(summ_dit)[1]

clusterA = [[], []]
for s in open('27A.txt'):
    [x, y] = [float(i) for i in s.split()]
    if y > 4:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(c) for c in clusterA]
PX = int((sum(abs(x) for x,y in centerA) / 2)*10_000)
PY =int((sum(abs(y) for x,y in centerA) / 2)*10_000)
print(PX,PY)



clusterB = [[], [],[]]
for s in open('B.txt'):
    [x, y] = [float(i) for i in s.split()]
    if x < 0:
        clusterB[0].append([x, y])
    elif y> 8:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(c) for c in clusterB]
PX = int((sum(abs(x) for x,y in centerB) / 3)*10_000)
PY =int((sum(abs(y) for x,y in centerB) / 3)*10_000)
print(PX,PY)