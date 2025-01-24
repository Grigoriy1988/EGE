def f(a):
    bin_a = bin(a)[2:]
    if bin_a.count('1') % 2 == 0:
       bin_a = '10' + bin_a + '0'
    else:
        bin_a = '11' + bin_a
    return int(bin_a,2)

for i in range(100):
    if f(i) >= 58:
        print(f'{i} => {f(i)}')
        break