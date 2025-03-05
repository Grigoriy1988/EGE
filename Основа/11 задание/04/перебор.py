from  math import *

kod_bit = ceil(log2(26 + 26))
password = ceil(7 * kod_bit / 8)
user = password + 12
for count_user in range(1,10000):
    if count_user * user < 2 * 1024:
        print(count_user)
    else:
        break

