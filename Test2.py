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

if academic_discipline.get('Математика', None):
    print(
        "\n".join(f'{academic_discipline['Математика'].index(i) + 1}) {i}' for i in academic_discipline['Математика']))
else:
    print("Математику не изучает ни один студент")


