from itertools import  product
print(f'x\ty\tz\tf')
for x,y,z in product([0,1], repeat=3):
    f = (not x and y and z)or(not x and not z)
    f = int(f)
    if f == 1:
        print(f'{x}\t{y}\t{z}\t{f}')