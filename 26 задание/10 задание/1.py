f = open('26.txt')
n = int(f.readline())
student = dict()
for i in range(1000000):
    student[i] = set()
# print(student)
for i in range(n):
    student_num, num = map(int, f.readline().split())
    student[student_num].add(num)
# print(student)
new_student = {k: sorted(v) for k, v in student.items() if len(v) != 0}
# print(new_student[40031])
n = 0
maxcount = 0
for k, v in new_student.items():
    count = 1
    for номер in range(len(v) - 1):
        # print(v[номер], v[номер + 1] + 1)
        if v[номер] == v[номер + 1] - 1:
            count += 1
            if count > maxcount:
                n = k
                maxcount = count
        else:
            count = 1
print(n, maxcount)
# https://vk.com/ege_info_open?z=video-205865487_456240459%2F0bdc1ae31334af28f3%2Fpl_wall_-205865487
