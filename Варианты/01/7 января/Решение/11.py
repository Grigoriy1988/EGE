from  math import *
k = 8
N = 7
kod_bit = ceil(log2(N))
print(kod_bit,',бит на 1 символ')
I = ceil((k * kod_bit) / 8)  + 8
print(I * 42)
