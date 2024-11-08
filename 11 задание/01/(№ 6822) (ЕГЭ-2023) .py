from math import *

kod_bit = ceil(log2(52))
print(kod_bit, ',бит на символ минимум')
password_bait = ceil((10 * kod_bit) / 8)
print(password_bait,'байт на пароль')
res = (65_536 * password_bait) / 1024
print(res)
