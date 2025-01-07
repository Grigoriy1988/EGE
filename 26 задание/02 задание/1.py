f = open('26_838.txt')
N = int(f.readline())
a = [int(i) for i in f]
a.sort(reverse=True)
s =sum(a)//2
disk1 = []
disk2 = []
while a:
    disk1.append(a.pop(0))
    while sum(disk2) < sum(disk1) and len(a) != 0:
        disk2.append(a.pop(-1))
print(len(disk1),len(disk2))

