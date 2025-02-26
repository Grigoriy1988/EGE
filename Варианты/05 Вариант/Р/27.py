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
for s in open('27_A_17834.txt'):
    x, y = [float(c) for c in s.split()]
    if x < 6:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])
print(len(clusterA[0]) + len(clusterA[1]))
centerA = [center(cl) for cl in clusterA]
Px = sum(x for x, y in centerA) / 2
Py = sum(y for x, y in centerA) / 2
print(int(Px * 100), int(Py * 100))


clusterB = [[], [], []]
for s in open('27_B_17834.txt'):
    x, y = [float(c) for c in s.split()]
    if x > 4.5 and y > 2:
        clusterB[0].append([x, y])
    elif y > 1.8 and -3.1 <= x <= 3.1:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
Px = sum(x for x, y in centerB) / 3
Py = sum(y for x, y in centerB) / 3
print(int(Px * 100), int(Py * 100))
