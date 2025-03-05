from math import dist # dist - определяет расстояние
point  = []
for s in open('27_А.txt'):
    x ,y = [float(d) for d in s.split()]
    point.append([x,y])
# сбор кластеров
cluster = []
while point:
    cluster.append([point.pop(0)])
    for p in cluster[-1]:
        sosed_point = [p1 for p1 in point if dist(p,p1) < 1 ]
        cluster[-1].extend(sosed_point)
        for p1 in sosed_point:
            point.remove(p1)
print(len(cluster[0]), len(cluster[1]))

# поиск центра телескопа
def centr(cluser):
    m = []
    for p in cluser:
        k = 0
        for p1 in cluser:
            if dist(p,p1) <2.1:
               k+=1
        m.append([k,-dist(p,[0,0]),p])
    return max(m)[2]
centrT = [centr(cl) for cl in cluster]
print(centrT)

Px = sum(x for x,y in centrT ) / len(centrT)
Py = sum(y for x,y in centrT ) / len(centrT)

print(abs(int(Px*10000)),abs(int(Py*10000)))



point  = []
for s in open('27_Б.txt'):
    x ,y = [float(d) for d in s.split()]
    point.append([x,y])
# сбор кластеров
cluster = []
while point:
    cluster.append([point.pop(0)])
    for p in cluster[-1]:
        sosed_point = [p1 for p1 in point if dist(p,p1) < 1 ]
        cluster[-1].extend(sosed_point)
        for p1 in sosed_point:
            point.remove(p1)
print(len(cluster[0]), len(cluster[1]),len(cluster[2]))
centrT = [centr(cl) for cl in cluster]
print(centrT)

Px = sum(x for x,y in centrT ) / len(centrT)
Py = sum(y for x,y in centrT ) / len(centrT)

print(abs(int(Px*10000)),abs(int(Py*10000)))