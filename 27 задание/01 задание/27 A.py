# находим расстояние
def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# находим центр
def center(cluster):
    sum_dist = []
    for p in cluster:
        sm = sum(distance(p, p1) for p1 in cluster)
        sum_dist.append([sm, p]) # коментарий
    return min(sum_dist)[1]

# Заполняем кластер
clusterA = [[], []]
for s in open('27A.txt'):
    x, y = [float(c) for c in s.split()]
    if y > 8:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

# print(clusterA[0])
# print(clusterA[1])
# print(len(clusterA[0]) + len(clusterA[1]))

centerA = [center(cl) for cl in clusterA]
#print(centerA)
Px = sum(abs(x)  for x,y in centerA)/2
Py = sum(abs(y)  for x,y in centerA)/2
print(int(Px*10_000),int(Py*10_000))
#
# clusterB = [[], [],[]]
# for s in open('27B.txt'):
#     x, y = [float(c) for c in s.split()]
#     if y < 4:
#         clusterB[0].append([x, y])
#     elif x >5:
#         clusterB[1].append([x, y])
#     else:
#         clusterB[2].append([x,y])
#
# centerB = [center(cl) for cl in clusterB]
# #print(centerA)
# Px = sum(abs(x)  for x,y in centerB)/3
# Py = sum(abs(y) for x,y in centerB)/3
# print(int(Px*10_000),int(Py*10_000))
