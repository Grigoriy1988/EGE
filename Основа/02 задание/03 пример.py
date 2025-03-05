print(f'x\ty\tw\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = ((w <= y) <= x) or not (z)
                f = int(f)
                if f == 0:
                    print(f'{x}\t{y}\t{w}\t{z}\t{f}')
