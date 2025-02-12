f = open('3.txt')
d = dict()
for i in f:
    data , price = f.readline().split()
    if data in d:
        d[data] += int(price)
    else:
        d[data] = int(price)
print(max(d,key=d.get),d[max(d,key=d.get)])

