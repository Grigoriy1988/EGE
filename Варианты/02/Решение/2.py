# ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))
print(f'x\ty\tz\tw\tf')
for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = ((x <= y ) and (y <= w)) or (z == ( x or y))
                if int(f) == 0:
                    print(f'{x}\t{y}\t{z}\t{w}\t{int(f)}')

