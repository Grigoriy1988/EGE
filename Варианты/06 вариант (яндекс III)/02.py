# c ∧ (a∨d) ∧ (d→b)
def f(a,b,c,d):
    return int(c and (a or d) and (d <= b))
print(f'a\tb\tc\td\tf')
for a in 0,1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                if f(a,b,c,d):
                    print(f'{a}\t{b}\t{c}\t{d}\t{f(a,b,c,d)}')
