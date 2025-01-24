from math import *
k = 15
N = 10 + 25+25 + 6
i = ceil(log(N,2))
password = ceil(k * i/8)
dop  = 800/40 - password
print(dop)