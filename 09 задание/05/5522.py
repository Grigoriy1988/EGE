file = open('input.txt', mode='r')
answer = open('output.txt', mode='w')  # ('output.txt',mode='a')
count = 0
'''
– в строке только одно число повторяется трижды (ровно 3 раза), остальные числа не повторяются;
– утроенная сумма неповторяющихся чисел строки не больше произведения повторяющихся чисел.
'''
for string in file:
    a = [int(x) for x in string.split()]
    a_3 = [i for i in a if a.count(i)==3]
    a_unique = [i for i in a if a.count(i)==1]
    if (len(a_3) == 3 and len(a_unique) == 3) and (sum(a_unique)*3 <= a_3[0]**3):
        print(a_3,a_unique)
        count +=1
file.close()
answer.write(str(count)+'\t')
answer.close()
print(count)