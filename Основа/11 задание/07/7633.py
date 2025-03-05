from math import *
N = 10 + 52 + 963
kod_bit = ceil(log2(N))
id_count = 2000
I = 693 * 1024
for k in range(1,10000000):
    if id_count * ceil(k * kod_bit / 8) <= I:
        print(k)
    else:
        break
