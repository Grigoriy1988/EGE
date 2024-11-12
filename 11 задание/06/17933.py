from math import *
id_num = 1231 # длина серийного номера
count_num = 523872 # кол-во серийных номеров
I = 432* 1024*1024 # байт на все номера
for N in range(2,100):
    kod_bit = ceil(log2(N)) # бит на номер
    id_bait =  ceil((id_num * kod_bit) / 8)
    if count_num * id_bait > I:
        print(N,count_num * id_bait/1024/1024)

