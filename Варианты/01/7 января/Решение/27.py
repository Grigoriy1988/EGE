def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return abs(x2 - x1) + abs(y2 - y1)


# находим центр
def center(cluster):
    sum_dist = []
    for p in cluster:
        sm = sum(distance(p, p1) for p1 in cluster)
        sum_dist.append([sm, p,distance(p,(0,0))])
    # for a in sum_dist:
    #     if a[0] == min(sum_dist)[0]:
    #         print(a)
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
print(int(Px * 10000), int(Py * 10000))

clusterB = [[], [], []]
for s in open('27B.txt'):
    x, y = [float(c) for c in s.split()]
    if y>-2:
        clusterB[0].append([x, y])
    elif x>-3:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
# print(centerA)
Px = sum(x for x, y in centerB) / 3
Py = sum(y for x, y in centerB) / 3
print(int(Px * 10000), int(Py * 10000))
