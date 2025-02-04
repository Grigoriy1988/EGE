from math import *
f = open('27_А.txt')
data = []
for s in f:
    x, y = [float(c) for c in s.split()]
    data.append([x,y])
# print(data)
# находим расстояние
def distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def getCluster(p0):
    cluster = [p for p in data if distance(p0,p)<= 2]
    if len(cluster)>0:
        for p in cluster:
            data.remove(p)
        next_cluster = [getCluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster,[])
    return cluster

clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    clusters.append(cluster)
print(len(clusters[0]),len(clusters[1]))

# # находим центр
# def center(cluster):
#     sum_dist = []
#     for p in cluster:
#         sm = sum(distance(p, p1) for p1 in cluster)
#         sum_dist.append([sm, p])
#     return min(sum_dist)[1]
#
# # Заполняем кластер
# clusterA = [[], []]
# for s in open('27_А.txt'):
#     x, y = [float(c) for c in s.split()]
#     if x>0:
#         clusterA[0].append([x, y])
#     else:
#         clusterA[1].append([x, y])
#
# print(len(clusterA[0]) + len(clusterA[1]))
#
# centerA = [center(cl) for cl in clusterA]
# print(centerA)
# Px = sum(abs(x)  for x,y in centerA)/2
# Py = abs(sum(y  for x,y in centerA)/2)
# print(int(Px*10_000),int(Py*10_000))