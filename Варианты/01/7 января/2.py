# ((1≡w)≡(¬((w∧x)∨y)))→z
print('x\ty\tw\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = int(((1 == w) == (not ((w and x) or y))) <= z)
                print(f'{x}\t{y}\t{w}\t{z}\t{f}')
