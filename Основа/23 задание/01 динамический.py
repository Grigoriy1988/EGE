array = [0] * 11
array[2] = 1
for i in range(2,10):
    if i+1 <=10:
        array[i+1] += array[i]
    if i*2 <=10:
        array[i*2] += array[i]

print(array[2:])