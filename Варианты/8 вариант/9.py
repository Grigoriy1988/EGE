file = open('9.txt',mode='r')
count = 0
for sting in file:
    a = sorted([int(x) for x in sting.split()],reverse=True)
    b = [i for i in a if i % 2 ==0]
    c = [i for i in a if i % 2 !=0]
    if len(b) !=0 and max(b) < (sum(a) - max(b)) and (sum(b) == sum(c)):
        count +=1
print(count)