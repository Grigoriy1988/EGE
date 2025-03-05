from dee import div

for i in range(135790, 163228 + 1):
    d = div(i)[1:-1]
    if sum(d) > 460000:
        print(f'{len(d)}  {sum(d)}')
