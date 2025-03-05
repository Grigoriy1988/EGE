from dee import div
for i in range(81234,134689+1):
    if len(div(i)) == 5:
        print(f'{i}: {div(i)[1]} {div(i)[3]}')
