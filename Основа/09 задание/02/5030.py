file = open('input.txt',mode='r')
answer = open('output.txt',mode='w') #('output.txt',mode='a')
count = 0
for sting in file:
    a = sorted([int(x) for x in sting.split()],reverse=True)
    # print(a)
    if a[0]==a[1] and a[2]==a[3] and a[4]==a[5]:
        print(a)
        count +=1
file.close()
answer.write(str(count)+'\n')
answer.close()
print(count)