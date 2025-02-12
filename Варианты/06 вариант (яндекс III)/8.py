from itertools import permutations
count = 0
for i in permutations('артём' ,5):
    if not(i[0] in 'аё' and i[-1] in 'аё'):
        print(i)
        count +=1

print(count)