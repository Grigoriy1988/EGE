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
for s in open("27A.txt"):
    x, y = [float(c) for c in s.split()]
    if (0 < x < 2 and -1 < y < 1) or (10 < x < 12 and 0 < y < 2):
        continue
    elif -1 < x < 3 and 2 < y < 9 or x < 7 and 2 < y < 5:
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
    if -1 < x < 1 and 9 < y < 11 or 7 < x < 9 and  -3 < y < -1 or 10 < x < 12 and 1 < y < 3:
        pass
    elif  y > 5.25:
        clusterB[0].append([x, y])
    elif 2 < x < 10 and 2 <= y <= 5.25 or x > 7:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
# print(centerA)
Px = sum(x for x, y in centerB) / 3
Py = sum(y for x, y in centerB) / 3
print(int(Px * 100000), int(Py * 100000))
