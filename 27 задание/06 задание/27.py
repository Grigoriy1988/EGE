def distance(p1,p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

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
    if x < 4 or (x < 6 and 2<y<4):
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(cl) for cl in clusterA]
#print(centerA)
Px = sum(x for x,y in centerA)/2
Py = sum(y for x,y in centerA)/2
print(int(Px*100000),int(Py*100000))


clusterB = [[], [],[]]
for s in open('27B.txt'):
    x, y = [float(c) for c in s.split()]
    if x < 1 or (x < 4 and  y< 2):
        clusterB[0].append([x, y])
    elif (x > 2 and y > 5)  or x > 7:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
#print(centerA)
Px = sum(x for x,y in centerB)/3
Py = sum(y for x,y in centerB)/3
print(int(Px*100000),int(Py*100000))