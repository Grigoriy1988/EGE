from math import*
N = 10 +26 + 230
i = ceil(log2(N))
for k in range(1,1000):
    if ceil(k * i / 8) * 506 > 63 * 1024:
        print(f'{k} -> {ceil(k * i / 8) * 506 / 1024}')