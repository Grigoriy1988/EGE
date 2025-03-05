array = [0] * 21
array[2] = 1
for i in range(2, 8):

    if i + 1 <= 8:
        array[i + 1] += array[i]
    if i * 2 <= 8:
        array[i * 2] += array[i]

for i in range(8, 20):

    if i + 1 <= 20:
        array[i + 1] += array[i]
    if i * 2 <= 20:
        array[i * 2] += array[i]
print(array[2:])
