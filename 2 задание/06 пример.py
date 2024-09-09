print(f'a\tb\tc\td\tf')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (a <=b)and(b <= (not c)) and((not c) <= d)
                f = int(f)
                if f == 1:
                    print(f'{a}\t{b}\t{c}\t{d}\t{f}')