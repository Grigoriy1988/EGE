'''
– в строке только одно число повторяется трижды, остальные числа различны;
– квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех её неповторяющихся чисел.
'''
file = open('input.txt', mode='r')
answer = open('output.txt', mode='w')  # ('output.txt',mode='a')
count = 0
for string in file:
    a = [int(i) for i in string.split()]
    a_3  = [i for i in a if a.count(i)==3]
    a_u = [i for i in a if a.count(i)==1]
    if (len(a_3)==3 and (len(a_u)==3)) and(sum(a_3)**2 > sum(a_u)**2):
        answer.write(', '.join(str(i) for i in a) + '\n')
        count +=1
answer.write(str(count))
answer.close()
file.close()
print(count)

