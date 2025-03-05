for n in range(1, 10):
    bin_n = bin(n)[2:]
    if sum(int(i) for i in bin_n) % 2 == 0:
        bin_n = bin_n + "0"
        bin_n = '10' + bin_n[2:]
    else:
        bin_n = bin_n + "1"
        bin_n = '11' + bin_n[2:]
    R = int(bin_n, 2)
    # print(f"N = {n}, bin_r = {bin_n}, R = {R}")
    if R >= 16:
        print(f"N = {n}, bin_r = {bin_n}, R = {R}")
