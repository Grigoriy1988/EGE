'''
НАЧАЛО
  ПОКА нашлось (25)
    заменить (25, 9)
  КОНЕЦ ПОКА
КОНЕЦ
Исходная строка содержит 12 пятерок и некоторое количество двоек, других цифр нет, точный порядок расположения пятерок и двоек неизвестен.
 После выполнения программы получилась строка с суммой цифр 122.
'''
s= '252525252525252525252525' + '2'* 7
k = s.count('2')
while '25' in s:
    s =s.replace('25','9',1)
print(sum(int(x) for x in s))
print(k)