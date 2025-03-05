f = open('26.txt')
n = int(f.readline())
student = dict()
for i in range(1000000):
    student[i] = set()
for i in range(n):
    student_num, num = map(int,f.readline().split())
    student[student_num].add(num)
new_student = {k: sorted(v) for k,v in student.items() if len(v)!=0}
# print(new_student)
id_num = 0
max_count = 0
for k, v in new_student.items():
    count = 1
    for num in range(len(v) - 1):
        if v[num] == v[num+1] - 1:
            count +=1
            if count > max_count:
                id_num = k
                max_count = count
        else:
            count = 1
print(id_num,max_count)
