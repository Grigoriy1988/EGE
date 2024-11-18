from math import *

N = 10 + 26 + 8164
kod_bit = ceil(log2(N))
id_count = 835
I = 156 *1024 # более
for k in range(1,1000):
    if ceil(k*kod_bit/8)*id_count > I:
        print(k,ceil(k*kod_bit/8)*id_count/1024)

