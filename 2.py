from random import shuffle
from datetime import *

d = datetime.now().strftime('%d-%m-%Y')
print(d)
f = open(d+ '.txt',mode='w',encoding='utf-8')
f.write(d +  '\n')
name = ['Авдеенко Михаил', 'Бурлянов Даниил', 'Гаврилов Артем', 'Кичко Анастасия', 'Коханец Владимир', "Морщинин Алан",
        "Пятков Артём", "Турецкий Андрей", "Цыганова Варвара", "Эльчапаров Артем"]
s = [8005,7560,7559,7480,7265,7260,6749,6639,6477,6473]
n = 0
shuffle(s)

for i in s:
    print(name[n], i)
    f.write(name[n] + ': ' + str(i) + '\n')
    n += 1
f.close()
#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat67=on&cat68=on&cat69=on&cat70=on&cat123=on&cat167=on
