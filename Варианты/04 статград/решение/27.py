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


def radius(p, cluster):
    r = []
    for i in cluster:
        r.append(distance(i, p))
    return max(r)


# Заполняем кластер
clusterA = [[], [], []]
for s in open('27A.txt'):
    x, y = [float(c) for c in s.split()]
    if x < 0:
        clusterA[0].append([x, y])
    elif 1 < x < 3:
        clusterA[1].append([x, y])
    else:
        clusterA[2].append([x, y])
# print(len(clusterA[0]), len(clusterA[1]), len(clusterA[2]))
clusterA.pop(1)
centerA = [center(cl) for cl in clusterA]
# print(centerA[0])
Ra = (radius(centerA[0], clusterA[0]), radius(centerA[1], clusterA[1]))
print(int(sum(Ra) / len(Ra) * 10_000))

# Заполняем кластер
clusterB = [[], [], [], [], []]
for s in open('27B.txt'):
    x, y = [float(c) for c in s.split()]
    if x < -2:
        clusterB[0].append([x, y])
    elif x > 4:
        clusterB[1].append([x, y])
    elif -1 < x < 2 and (2 < y < 4):
        clusterB[2].append([x, y])
    elif 2 < x < 4 and (2 < y < 5):
        clusterB[3].append([x, y])
    else:
        clusterB[4].append([x, y])
print(len(clusterB[0]), len(clusterB[1]), len(clusterB[2]),len(clusterB[3]),len(clusterB[4]))
clusterB.pop(4)
centerB = [center(cl) for cl in clusterB]
print(centerB[0])
Rb=[]
for i in range(len(clusterB)):
    Rb.append(radius(centerB[i],clusterB[i]))
print(Rb)
# Rb = (radius(i,j) for i in clusterB for j in clusterB)
# print(*Rb)
print(int(sum(Rb) / len(Rb) * 10_000))
