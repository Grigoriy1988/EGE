from math import *
file = open('input.txt')
k = 0
for sting in file:
    even = [int(i) for i in sting.split() if int(i) % 2 == 0]
    odd = [int(i) for i in sting.split() if int(i) % 2 != 0]
    # print(prod(odd))

    if (len(even) >= 2 and len(odd) >=2) and (3*sum(odd) > prod(even)):
        k+=1
        print(sting)
print(k)
