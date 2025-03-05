from math import dist  # dist - определяет расстояние

point = []
for s in open('27_A.txt'):
    x, y = [float(d) for d in s.split()]
    point.append([x, y])
# сбор кластеров
cluster = []
while point:
    cluster.append([point.pop(0)])
    for p in cluster[-1]:
        sosed_point = [p1 for p1 in point if dist(p, p1) < 5.5]
        cluster[-1].extend(sosed_point)
        for p1 in sosed_point:
            point.remove(p1)
print([len(i) for i in cluster])


def kor(cl):
    xavg = sum(x for x, y in cl) / len(cl)
    yavg = sum(y for x, y in cl) / len(cl)
    ch = sum((x - xavg) * (y - yavg) for x, y in cl)
    znam = (sum((x - xavg) ** 2 for x, y in cl) * sum((y - yavg) ** 2 for x, y in cl)) ** 0.5
    return ch / znam
k = [kor(cl) for cl in cluster]
print(k)
k = [i for i in k if abs(i) > 0.9]
print(k)
print(len(k), sum(k) / len(k) * 100000)