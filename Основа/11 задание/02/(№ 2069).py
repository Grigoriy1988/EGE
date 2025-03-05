from math import *
kod_bit = ceil(log2(10+26+26))
print(kod_bit, ',бит на 1 символ')
password = ceil(10*6 / 8)
print(password,'байт на пароль')
user = 870 / 30
print(user,'байт на 1 пользователя')
print(user - password, 'байт на доп. сведенья ')