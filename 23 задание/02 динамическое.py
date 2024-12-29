array = [0] * 17
array[2] = 1
for i in range(2,16):
    if i == 4:
        array[i] =0
    if i+1 <=16:
        array[i+1] += array[i]
    if i*2 <=16:
        array[i*2] += array[i]

print(array[2:])