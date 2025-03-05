file = open('input.txt')
answer = open('output.txt',mode='w') #('output.txt',mode='a')
count = 0
for sting in file:
    a = sorted([int(x) for x in sting.split()])
    # print(a)
    if (a[0] != a[1] != a[2] != a[3]) and (a[3]+a[0] > a[1]+a[2]):
        print(a)
        count +=1
file.close()
answer.write(str(count)+'\n')
answer.close()
print(count)

