def f (x,y,z,w):
    return int((not(x <= y)) or (z==w) or z)
print(f'x\ty\tz\tw\tf')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x,y,z,w) == 0:
                    print(f'{x}\t{y}\t{z}\t{w}\t{f(x,y,z,w)}')