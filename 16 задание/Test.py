def f(n):
    if n <=5:
        return n
    elif n % 8 == 0:
        return n + f(n//2 -3)
    return  n + f(n + 4)
for i  in range(10000):
    try:
        print(i, f(i))
    except:
        pass

        #print("Ошибка ", i)
