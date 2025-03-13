from random import shuffle, choice
from datetime import *

d = datetime.now().strftime('%d-%m-%Y')
print(d)
f = open(d + '.txt', mode='w', encoding='utf-8')
f.write(d + '\n')
name = ['Авдеенко Михаил', 'Бурлянов Даниил', 'Гаврилов Артем', 'Кичко Анастасия', 'Коханец Владимир', "Морщинин Алан",
        "Пятков Артём", "Турецкий Андрей", "Цыганова Варвара", "Эльчапаров Артем"]
задание1 = [4881, 4880, 4879, 4871, 3434, 385, 381, 380, 368]
задание2 = [7481, 5921, 3835, 3830, 3830, 3827, 3605, 3601, 2988]
задание3 = [6301, 4023, 7262, 7261, 7260, 7259, 7259, 7257, 7255]
for i in name:
    shuffle(задание1)
    shuffle(задание2)
    shuffle(задание3)
    s = задание1[:3] + задание2[:3] + задание3[:3]
    print(i, ', '.join(str(n) for n in s))
    f.write(i +':   '+ ', '.join(str(n) for n in s) + '\n')

f.close()

# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat68=on
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat69=on
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat70=on
