dig ='0123456789abcdefghijk'
# print(len(dig))
for p in range(9,22):
    for x in dig[:p]:
        for y in dig[:p]:
            for w in dig[:p]:
                for z in dig[:p]:
                    a = f"{y}27{x}"
                    b = f"{w}{y}86"
                    c = f'{x}{x}{z}3{y}'
                    if int(a,p)+int(b,p)==int(c,p):
                        print(f"{x} {y} {w} {z} основание {p}")
                        print(f'xyzw = {int(f'{x}{y}{z}{w}',p)}')
