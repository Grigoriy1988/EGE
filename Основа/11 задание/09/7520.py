from math import *
k = 261
id_count = 252500
I = 31 * 1024 *1024 # более
N_list = []
for N in range(2,1000):
    kod_bit = ceil(log2(N))
    if ceil(k*kod_bit / 8)* id_count > I:
        N_list.append(N)
        print(N,id_count*ceil(k*kod_bit / 8)/1024/1024)
print(N_list)