point = 1024*768
k = 27
v =  1638400 # бит/с
t = 220 # не более с
for i in range(1,32):
    I = point * i * k
    if I/v <= t:
        print(f'i = {i}')
    else:
        break
print(2**(i-1))