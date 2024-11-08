from math import *

kod_bit = ceil(log2(10 + 4090))
print(kod_bit, ',бит на 1 символ')
password = ceil(101 * kod_bit / 8)
print(password,'байт на пароль')
print(2048 * password / 1024, 'Кбайт на 2048 пользователей')