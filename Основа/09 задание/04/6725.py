file = open('input.txt', mode='r')
answer = open('output.txt', mode='w')  # ('output.txt',mode='a')
count = 0
'''
– квадрат суммы наибольшего и наименьшего чисел меньше суммы квадратов трёх других.
'''
for sting in file:
    a = sorted([int(x) for x in sting.split()])
    # print(a)
    a_2 = [i for i in a if a.count(i) == 2]
    a_unique = [i for i in a if a.count(i) == 1]
    if (len(a_2)==2 and len(a_unique)==3) and((a[0]+a[4])**2< a[1]**2 + a[2]**2 + a[3]**2):
        print(a_2,a_unique)
        count+=1
file.close()
answer.write(str(count)+'\t')
answer.close()
print(count)