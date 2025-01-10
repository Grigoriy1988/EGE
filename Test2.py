academic_discipline = {}

while True:
    a = input('Введите название предмета или нажмите enter\n>> ')
    if a:
        academic_discipline[a] = []
        while True:
            surname = input("Введите фамилию или нажмите enter\n>> ")
            if surname:
                academic_discipline[a].append(surname)
            else:
                break
    else:
        break
print(academic_discipline)

