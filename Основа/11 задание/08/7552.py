from math import *

N = 10 + 2030
kod_bit = ceil(log2(N))
id_count = 318
I = 67 * 1024 # более!
k_list = []
for k in range(2,10000):
    if ceil(k*kod_bit / 8)* id_count > I:
        k_list.append(k)
print(min(k_list))