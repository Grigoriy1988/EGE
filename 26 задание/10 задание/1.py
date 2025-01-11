f = open('26.txt')
n = int(f.readline())
student = dict()
# Создаем словарь где ключами будут идентификаторы, а значениями — множество номеров правильно решённых задач
for i in range(1000000):
    student[i] = set()

for i in range(n):
    student_num, num = map(int, f.readline().split())
    student[student_num].add(num)
# удаляем всех студентов с нерешенными задачами
new_student = {k: sorted(v) for k, v in student.items() if len(v) != 0}

id_num = 0   # Искомый идентификационный номер
max_count = 0 # наибольшее количество задач с идущими подряд номерами
for k, v in new_student.items():
    count = 1
    for num in range(len(v) - 1):
        if v[num] == v[num + 1] - 1:
            count += 1
            if count > max_count:
                id_num = k
                max_count = count
        else:
            count = 1
print(id_num, max_count)










# https://vk.com/ege_info_open?z=video-205865487_456240459%2F0bdc1ae31334af28f3%2Fpl_wall_-205865487
