# (x ˅ ¬y) ˄ ¬(x ≡ z) ˄ ¬w
print(f'x\ty\tw\tz\tf')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (x or not y) and not (x==z) and not w
                f = int(f)
                if f == 1:
                    print(f'{x}\t{y}\t{w}\t{z}\t{f}')