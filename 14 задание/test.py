for n in range(2,37):
   try:
       if (7 ** 500 - int('53', n)) % 6 == 0:
           print(n)
   except:
       print(f"При {n} ошибка")