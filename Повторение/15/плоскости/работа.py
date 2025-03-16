from random import shuffle
from datetime import *
d = datetime.now().strftime('%d-%m-%Y')
print(d)
f = open(d + '.txt', mode='w', encoding='utf-8')
f.write(d + '\n')
name = ['Авдеенко Михаил', 'Бурлянов Даниил', 'Гаврилов Артем', 'Кичко Анастасия', 'Коханец Владимир', "Морщинин Алан",
        "Пятков Артём", "Турецкий Андрей", "Цыганова Варвара", "Эльчапаров Артем"]
s = [7560,6748,6747,5356,4494,1066,1064,1061]
for i in name:
    shuffle(s)
    print(i, ', '.join(str(n) for n in s[:5]))
    f.write(i + ': ' + ', '.join(str(n) for n in s[:5]) + '\n')

f.close()
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat123=on