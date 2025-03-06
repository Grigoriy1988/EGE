from random import shuffle

name = ['Авдеенко Михаил', 'Бурлянов Даниил', 'Гаврилов Артем', 'Кичко Анастасия', 'Коханец Владимир', "Морщинин Алан",
        "Пятков Артём", "Турецкий Андрей", "Цыганова Варвара", "Эльчапаров Артем"]
s = [8005,7560,7559,7480,7265,7260,6749,6639,6477,6473]
n = 0
shuffle(s)

for i in s:
    print(name[n], i)
    n += 1
#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat67=on&cat68=on&cat69=on&cat70=on&cat123=on&cat167=on
