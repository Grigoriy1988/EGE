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
        sosed_point = [p1 for p1 in point if dist(p, p1) < 50]
        cluster[-1].extend(sosed_point)
        for p1 in sosed_point:
            point.remove(p1)
print([len(i) for i in cluster])
cluster = [i for i in cluster if len(i) > 1000]
print([len(i) for i in cluster])


def plotnost(cl):
    m = []
    for p in cl:
        for p1 in cl:
            if p1 != p:
                m.append(dist(p1, p))
    avg = sum(m) / len(m)
    return avg / max(m)


pl = [plotnost(cl) for cl in cluster]
print(int(min(pl) * 10000), int((sum(pl) / len(pl) * 10000)))



point = []
for s in open('27_B.txt'):
    x, y = [float(d) for d in s.split()]
    if 1000 < x < 2100 and 1500 < y <4500 or  3000 < x < 5200 and 5000 < y <8000 or  6500 < x < 9200 and 3500 < y <6000:
        point.append([x, y])
# сбор кластеров
cluster = []
while point:
    cluster.append([point.pop(0)])
    for p in cluster[-1]:
        sosed_point = [p1 for p1 in point if dist(p, p1) < 50]
        cluster[-1].extend(sosed_point)
        for p1 in sosed_point:
            point.remove(p1)
print([len(i) for i in cluster])
cluster = [i for i in cluster if len(i) > 1000]
print([len(i) for i in cluster])
pl = [plotnost(cl) for cl in cluster]
print(int(min(pl) * 10000), int((sum(pl) / len(pl) * 10000)))