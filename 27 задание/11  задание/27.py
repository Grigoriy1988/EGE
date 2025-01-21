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
    if (1 < x < 3 and 2 < y < 3) or (7 < x < 8 and -2 < y <-1):
        continue
    elif  x < 5.5 and y >= 0 or x < 3.5:
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
    if 2.5 < x < 3.5 and 8.5 < y < 9.5 or 10 < x < 11 and  9.5 < y < 10.5 or 9.5 < x < 10.5 and -3.5 < y < -2.5:
        pass
    elif  4.5 < x < 8 and 2<y<7:
        clusterB[0].append([x, y])
    elif 1 < x < 8 and -2 <= y <= 6:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

centerB = [center(cl) for cl in clusterB]
# print(centerA)
Px = sum(x for x, y in centerB) / 3
Py = sum(y for x, y in centerB) / 3
print(int(Px * 100000), int(Py * 100000))
