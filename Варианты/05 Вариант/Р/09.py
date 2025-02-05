f = open('9.txt')
count = 0
for s in f:
   a = sorted([int(i) for i in s.split()])
   b = [i for i in a if i % 10 == 5]
   if len(b)
