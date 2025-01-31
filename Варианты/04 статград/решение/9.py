f = open('9.txt')
count = 0
for s in f:
    a = [int(x) for x in s.split()]
    if a.count(max(a)) == 1 and max(a) in a[:4] and sum(a[:4]) < sum(a[4:]):
        count +=1
print(count)


