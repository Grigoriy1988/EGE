for n in range(1, 50):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'

    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'
    R = int(bin_n, 2)
    # print(n, bin_n,R)
    if R > 130:
        print(n, bin_n, R)
        # break
