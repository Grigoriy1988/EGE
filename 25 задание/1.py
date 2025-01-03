from dee import div
for i in range(193136,193223+1):
    if len(div(i)) == 6:
        print(f'{i} делители: {', '.join(str(k) for k in div(i))}')
