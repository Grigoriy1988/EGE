def f(a):
    bin_a = bin(a)[2:]
    if bin_a[-1] == '0':
        bin_a = bin_a + '0' * bin_a.count("0")
    else:
        bin_a = '1' * bin_a.count("1") + bin_a
    return int(bin_a,2)


for i in range(1,10000):
    if f(i) > 2000:
        print(i)
        break
