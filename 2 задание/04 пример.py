print(f'x\ty\tw\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (not x and y and z and not w) or (not x and y and not z and not w) or (x and y and z and not w)
                f = int(f)
                if f == 1:
                    print(f'{x}\t{y}\t{w}\t{z}\t{f}')