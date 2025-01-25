file = open('9.txt')
count = 0
for sting in file:
    a = [int(x) for x in sting.split()]
    odd = [i for i in a if i % 2 !=0]
    unique = [i for i in a if a.count(i)==1]
    if (len(odd) == 3 and len(a) == len(unique))or (len(odd) != 3 and len(a) != len(unique)):
        print(a)
        count +=1
print(count)