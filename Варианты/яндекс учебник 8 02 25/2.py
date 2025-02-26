#(x→y)∧(w∨(¬w))
def F(x,y,w):
    return int((x<=y)and(w or (not w)))
print(f'x\ty\tw\tf')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            f = F(x,y,w)
            print(f'{x}\t{y}\t{w}\t{f}')