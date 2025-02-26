f = open('24.txt').readline()
for a in '+*':
    for b in '+*':
        while a + b in f:
            f = f.replace(a + b, f'{a} {b}')
f = f.split()
# print('\n'.join(f))
print(max(len(i) for i in f ))
