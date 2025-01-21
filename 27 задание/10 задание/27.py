def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


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
    if (-3 < x < -1 and -4 < y < -2) or (2 < x < 4 and 1 < y < 3):
        continue
    elif -3 < x <1 and -1 < y < 3:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

centerA = [center(cl) for cl in clusterA]
# print(centerA)
Px = sum(x for x, y in centerA) / 2
Py = sum(y for x, y in centerA) / 2
print(int(Px * 100000), int(Py * 100000))

clusterB = [[], [], []]
for s in open('27B.txt'):
    x, y = [float(c) for c in s.split()]
    if -4 < x <-2 and 5 < y < 7 or 4 <x < 6 or 6<y<8 or -2 <x<0 and -5 <y < -3:
        pass
    elif x <= 0.5 and -1 < y < 3 or x < 1 and 0 < y <= 2.5 :
        clusterB[0].append([x, y])
    elif y < 0:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
# print(centerA)
Px = sum(x for x, y in centerB) / 3
Py = sum(y for x, y in centerB) / 3
print(int(Px * 100000), int(Py * 100000))
