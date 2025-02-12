f = open('9.txt')
count = 0
for line in f:
    a = sorted([int(i) for i in line.split()])
    if len(set(a)) == len(a) and a[0]+ a[3] <= a[1]+a[2]:
      print(a)
      count+=1
print(count)
