file = open('9.txt', mode='r')
count = 0
for string in file:
    a = [int(x) for x in string.split()]
    dubl = [i for i in a if a.count(i)==2]
    s = sum(i for i in a if i not in dubl)
    if len(dubl)==2 and s % 2 == 0:
        count +=1
print(count)