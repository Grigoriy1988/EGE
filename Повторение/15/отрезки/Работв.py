from random import shuffle
from datetime import *
d = datetime.now().strftime('%d-%m-%Y')
print(d)
f = open(d + '.txt', mode='w', encoding='utf-8')
f.write(d + '\n')
name = ['Авдеенко Михаил', 'Бурлянов Даниил', 'Гаврилов Артем', 'Кичко Анастасия', 'Коханец Владимир', "Морщинин Алан",
        "Пятков Артём", "Турецкий Андрей", "Цыганова Варвара", "Эльчапаров Артем"]
s = [7837, 7836, 7835, 7834, 7833, 7832, 7831, 7830, 7829, 7828, 7828, 6482, 6481, 6480, 6479, 6478]
for i in name:
    shuffle(s)
    print(i, ', '.join(str(n) for n in s[:5]))
    f.write(i + ': ' + ', '.join(str(n) for n in s[:5]) + '\n')

f.close()
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat67=on&cat68=on&cat69=on&cat70=on&cat123=on&cat167=on
