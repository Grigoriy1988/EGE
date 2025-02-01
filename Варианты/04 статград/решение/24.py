f = open('24.txt').readline()
for a in '*+-':
    for b in '*+-':
        f = f.replace(a+b,' ')
f = f.replace('B',' ').replace('C',' ').replace('D',' ').split()
f = [i for i in f if 'A' in i and len(i)>1]
for i in f:
    print(i)
print(len(f))