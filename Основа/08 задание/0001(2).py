# модуль итераторов
from itertools import *
step = 1
for x in product("ЛТ","ЛЕТО","ЛЕТО","ЛЕТО"):

    print(f'{step} {x}')
    s = ''.join(x)
    step+=1