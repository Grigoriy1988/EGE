count = 0
for n in range(1,1000):
    bin_n = bin(n)[2:]
    s = sum(int(i) for i in bin_n) #sum(map(int,bin_n)
    bin_n = bin_n + str(s%2)
    #print(f"N = {n}, bin_r = {bin_n}, s = {s}")
    s = sum(int(i) for i in bin_n)
    bin_n = bin_n + str(s % 2)
    #print(f"N = {n}, bin_r = {bin_n}, s = {s}")
    R = int(bin_n,2)
    #print(f"N = {n}, bin_r = {bin_n}, R = {R}")
    if 210<=R<=260:
        count +=1
        print(f"N = {n}, bin_r = {bin_n}, R = {R} count = {count}")

