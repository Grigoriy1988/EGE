from math import *
# l = 256
# N = 10+4080
# i = ceil(log2(N))
# I = ceil((l* i)/8)
# print((2**16 * I)/(1024*1024))
k = 23
l = 500_000
I = 21* 1024 *1024
for i in range(1,20):
    if ceil(i*k/8)*l <= I:
        print(i,ceil(i*k/8)*l / 1024 /1024)