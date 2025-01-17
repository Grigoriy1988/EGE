# находим расстояние
def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return max(abs(x1 - x2), abs(y1 - y2))


# находим центр
def center(cluster):
    sum_dist = []
    for p in cluster:
        sm = sum(distance(p, p1) for p1 in cluster)
        sum_dist.append([sm, p])
    return min(sum_dist)[1]

clusterA = [[], []]
for s in open('27A.txt'):
    x ,y = [float(c) for c in s.split()]
    if -3<=x<=2:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(cl) for cl in clusterA]
Px = sum(x  for x,y in centerA)/2
Py = sum(y  for x,y in centerA)/2
print(int(Px*10_000),int(Py*10_000))


clusterB = [[], [],[]]
for s in open('27B.txt'):
    x ,y = [float(c) for c in s.split()]
    if x> 3.5:
        clusterB[0].append([x, y])
    elif y > -2.5:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
Px = sum(x  for x,y in centerB)/3
Py = sum(y  for x,y in centerB)/3
print(int(Px*10_000),int(Py*10_000))