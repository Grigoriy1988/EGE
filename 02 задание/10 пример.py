# (z≡¬x)→((w→¬y)∧(y→x))
print(f'x\ty\tw\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (z == (not x))<=((w<=(not y))and(y<=x))
                f = int(f)
                print(f'{x}\t{y}\t{w}\t{z}\t{f}')