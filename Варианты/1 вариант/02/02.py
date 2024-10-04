#(¬𝑐≡𝑑)∧ (𝑎∨𝑏) ∧(𝑏→𝑐)
print(f'a\tb\tc\td\tf')
for a in 0,1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f =(not c== d)and (a or b) and (b <= c)
                f = int(f)
                if f:
                    print(f'{a}\t{b}\t{c}\t{d}\t{f}')
