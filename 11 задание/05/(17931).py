from  math import *
kod_bit = ceil(log2(10 + 52+1988))
print(kod_bit,',бит на 1 символ')
count_id =1974
for id_number in range (1,1000):
    if ceil(kod_bit * id_number/8)*count_id <=579 * 1024:
        print(id_number)
    else:
        break
