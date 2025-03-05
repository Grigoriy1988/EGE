from math import *
kod_bit = ceil(log2(26 + 26))
print(kod_bit,',бит на 1 символ')
password = ceil(7 * kod_bit / 8)
print(password,'байт на пароль')
user = password + 12
print(user,'байт на пользователя')
count_user = 2 * 1024  /18
print(floor(count_user)) # округление в меньшую сторону 