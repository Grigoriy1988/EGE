from math import *
k = 197
count_num = 178080
I = 25 * 1024*1024 # Отведено более 25 Мбайт памяти
for i in range(1,10000):
    один = ceil((k * i)/8)
    if I >= один * count_num:
        print(i,один * count_num/ 1024/1024)
print(2**5, 2**6)