from itertools import *
count = 0
for i in product('0123456789abcde', repeat=5):
    n = ''.join(i)
    # print(n)
    for j in 'abcde':
        n = n.replace(j,'A')
    if n[0]!="0" and n.count("A") >= 2 and n.count('8') == 1:
        count +=1
print(count)