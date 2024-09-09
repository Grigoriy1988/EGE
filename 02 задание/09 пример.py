# x→y∧z
print(f'x\ty\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = x <= (y and z)
            f = int(f)
            if f == 0:
                print(f'{x}\t{y}\t{z}\t{f}')

