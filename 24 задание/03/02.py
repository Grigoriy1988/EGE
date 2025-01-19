# подбор
s = open('24_1040.txt').readline()
s = s.replace('1', '0').replace('2', '0').replace('3', '0').replace('4', '0').replace('5', '0').replace('6',
                                                                                                        '0').replace(
    '7', '0').replace('8', '0').replace('9', '0')
for i in range(1, 100):
    if '0' * i in s:
        print(i)
    else:
        break
