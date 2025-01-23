def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# находим центр
def center(cluster):
    sum_dist = []
    for p in cluster:
        sm = sum(distance(p, p1) for p1 in cluster)
        sum_dist.append([sm, p,distance(p,(0,0))])
    for a in sum_dist:
        if a[0] == min(sum_dist)[0]:
            print(a)
    return min(sum_dist)[1]


clusterA = [[], []]
for s in open("27A.txt"):
    x, y = [float(c) for c in s.split()]
    if x > 0:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(cl) for cl in clusterA]
# print(centerA)
Px = sum(x for x, y in centerA) / 2
Py = sum(y for x, y in centerA) / 2
print(int(abs(Px) * 10000), int(abs(Py) * 10000))

clusterB = [[], [], []]
for s in open('27_Б.txt'):
    x, y = [float(c) for c in s.split()]
    if -7 < x < -2 and -3<y<2.5:
        clusterB[0].append([x, y])
    elif -2.5 < x < 2.5 and 1.5 <= y <= 6.5:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
# print(centerA)
Px = sum(x for x, y in centerB) / 3
Py = sum(y for x, y in centerB) / 3
print(int(abs(Px) * 10000), int(abs(Py) * 10000))
