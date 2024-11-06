'''
– в строке ровно три числа кратны трём;
– диапазон чисел строки (разность между наибольшим и наименьшим значениями) не больше, чем сумма чисел строки, кратных 3
'''
file = open('input.txt', mode='r')
answer = open('output.txt', mode='w')  # ('output.txt',mode='a')
count = 0
for string in file:
    a = sorted([int(i) for i in string.split()])
    a_3 = [i for i in a if i % 3 == 0]
    if len(a_3) == 3 and (a[5]-a[0] <= sum(a_3)):
        print(a)
        count +=1
answer.write(str(count))
answer.close()
file.close()
print(count)