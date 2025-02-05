f = open('9.txt')
count = 0
for s in f:
   a = sorted([int(i) for i in s.split()])
   b = [i for i in a if i % 10 == 5]
   if len(b)>=2 and 2*(a[4]+a[3]) > 3*(a[0]+a[1]+a[2]):
      print(*a)
      count+=1
print(count)
