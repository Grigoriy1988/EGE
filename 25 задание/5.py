from dee import div

count = 0
i = 850_001
while count < 6:
    d = div(i)[1:-1]
    F = d[-1] - d[0] if len(d)>2 else 0 # max(d) - min(d) if len(d)>2 else 0  
    if F != 0 and F % 3 == 0:
        count += 1
        print(f'{count}) {i} => {F}')
    i += 1
