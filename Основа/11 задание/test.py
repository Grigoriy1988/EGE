# (№ 7552) (ЕГЭ-2024)
from math import *
N = 10 + 2030
i = ceil(log2(N)) # кол - во бит на 1 символ
id_count = 318 # кол - во серийных номеров
I_all  = 67 * 1024 #  отведено более 67 Кбайт памяти
k_id_list = []
for k in range(1, 1000):
    if ceil(k * i / 8) * id_count > I_all:
        k_id_list.append(k)
print(k_id_list)

