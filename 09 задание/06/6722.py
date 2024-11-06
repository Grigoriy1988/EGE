'''
– в строке есть только одно число, которое повторяется дважды, остальные четыре числа различны;
– повторяющееся число строки не меньше, чем среднее арифметическое четырёх её неповторяющихся чисел.
'''
file = open('input.txt', mode='r')
answer = open('output.txt', mode='w')  # ('output.txt',mode='a')
n = 0
for string in file:
    n += 1
    a = [int(x) for x in string.split()]
    a_2 = [x for x in a if a.count(x)==2]
    a_u = [x for x in a if a.count(x)==1]
    if (len(a_u)==4 and len(a_2)==2) and(a_2[0] >= (sum(a_u) / 4)):
        print(n)
        answer.write(', '.join(str(i) for i in a ) + '\t #' + str(n)+ '\n')
answer.close()
file.close()

