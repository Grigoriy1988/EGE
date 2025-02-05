print(f'x\ty\tw\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = int((y <= x) and (not (w)) and z)
                if f:
                    print(f'{x}\t{y}\t{w}\t{z}\t{f}')
