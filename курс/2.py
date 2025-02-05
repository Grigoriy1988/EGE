from random import choice

character = ['дружелюбный динозавр Вася', 'мальчик Вовочка', 'директор школы Андрей Иванович']
action = ['залез на крышу', 'получил двойку', 'объел клумбу']
descriptions = ['в красивой шляпе', 'утром понедельника', 'тайком от мамы']
print('\n'.join(character))
print('\n'.join(action))
print('\n'.join(descriptions))
for _ in range(4):
    print(choice(character), choice(action), choice(descriptions))
