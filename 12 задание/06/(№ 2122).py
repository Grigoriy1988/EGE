'''
НАЧАЛО
  ПОКА нашлось (56) ИЛИ нашлось (1111)
    заменить (56, 1)
    заменить (1111, 1)
  КОНЕЦ ПОКА
КОНЕЦ
состоящей из 102 строк 561
'''
s = '561' * 102
while '56' in s or '1111' in s:
    s = s.replace('56','1',1)
    s = s.replace('1111', '1', 1)
print(s)