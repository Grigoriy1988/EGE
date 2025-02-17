from math import *
k = 21
N = 26 + 26
i = ceil(log2(N))
print(f'{i} бит на символ') #
I = 80 * 1024  # не более байт на партию

for j in range(1, 20):

    if I >= (ceil((k * i + j) / 8) +  60) * (2 ** j) :
        print(j, (ceil((k * i + j) / 8) +  60) * (2 ** j))
    else:
        print('Ответ')
        for count in range(2 ** (j-1) + 1 ,2 ** j):
            if I>= (ceil((k * i + j) / 8) +  60)* count:
                print(count,j, (ceil((k * i + j) / 8) +  60)* count)

        break





