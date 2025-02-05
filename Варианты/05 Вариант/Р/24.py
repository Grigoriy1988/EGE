f = open('24.txt').readline()
for a in '+*':
    for b in '+*':
        f = f.replace(a + b, f'{a} {b}')
f = f.split()
print(max(len(i) for i in f ))
