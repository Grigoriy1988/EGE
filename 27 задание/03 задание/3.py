# находим расстояние
def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# находим центр
def center(cluster):
    sum_dist = []
    for p in cluster:
        sm = sum(distance(p, p1) for p1 in cluster)
        sum_dist.append([sm, p])
    return min(sum_dist)[1]


clusterA = [[], []]
for s in open('27A.txt'):
    x, y = [float(c) for c in s.split()]
    if y >3*x + 4:# x>0.5 and y <6.5
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(cl) for cl in clusterA]

Px = sum(x  for x,y in centerA)/2
Py = sum(y  for x,y in centerA)/2
print(int(Px*10_000),int(Py*10_000))

clusterB = [[], [],[]]
for s in open('27B.txt'):
    x,y = [float(c) for c in s.split()]
    if y > 0.5 and x < 8.5:
        clusterB[0].append([x,y])
    elif 4*y > -3*x + 28 :
        clusterB[1].append([x,y])
    else:
        clusterB[2].append([x, y])
print(clusterB[0][:10])
print(clusterB[1][:10])
print(clusterB[2][:10])
centerB = [center(cl) for cl in clusterB]

Px = sum(x  for x,y in centerB)/3
Py = sum(y  for x,y in centerB)/3
print(int(Px*10_000),int(Py*10_000))