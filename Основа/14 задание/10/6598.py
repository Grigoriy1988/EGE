for n in range(2, 27):
    try:
        if (7 ** 500 - int('53', n)) % 6 == 0:
            print(n)
    except:
        print(n, 'Error')
