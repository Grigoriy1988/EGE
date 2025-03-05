for n in range(1, 50):
    bin_n = bin(n)[2:]
    bin_n = bin_n + bin_n[-1]
    if bin(n)[2:].count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'

    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'
    R = int(bin_n, 2)
    if R > 90:
        print(f"N = {n}, bin_r = {bin_n}, R = {R}")
