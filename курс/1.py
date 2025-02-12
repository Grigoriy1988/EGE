for x in range(1, 100):
    for y in range(1,100):
        for z in range(1, 100):

            s = '1' + '5' * x + '6' * y + '7' * z
            # print(s)
            while '15' in s or '16' in s or '17' in s:
                s = s.replace('15', '7616', 1)
                s = s.replace('16', '51', 1)
                s = s.replace('17', '615', 1)

        # print(f'{x} {y} {z} {s}')
        # print(f'{s.count("5")} {s.count("6")} {s.count("7")} {s}')
            if s.count('7') == 109 and s.count('6') == 153 and s.count('5') == 126 and s.count('1') == 1:
                print(y)
