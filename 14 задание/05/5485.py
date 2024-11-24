# через int
for x in '0123456789ABCDEFGH':
    a = int('9009' + x,18) + int('2257'+x,18)
    if a %15 ==0:
        print(x, a /15)
