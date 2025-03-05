print(f'x\ty\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x and y and z) or (not x and not z)
            f = int(f)
            if f == 1:
                print(f'{x}\t{y}\t{z}\t{f}')
