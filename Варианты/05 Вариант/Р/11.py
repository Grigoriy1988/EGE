from math import *
l = 256
N = 10+4080
i = ceil(log2(N))
I = ceil((l* i)/8)
print((2**16 * I)/(1024*1024))