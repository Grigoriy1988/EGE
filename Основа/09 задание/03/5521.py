file = open('input.txt', mode='r')
answer = open('output.txt', mode='w')  # ('output.txt',mode='a')
count = 0
for sting in file:
    a = sorted([int(x) for x in sting.split()], reverse=True)
    a_2 = [i for i in a if a.count(i) == 2]
    a_уникальные = [i for i in a if a.count(i) == 1]
    # print(a, a_2, a_уникальные)
    if (len(a_2) == 2 and len(a_уникальные) == 4) and (sum(a_уникальные)/4 <= sum(a_2)):
        print(a_2, a_уникальные)
        count += 1
file.close()
answer.write(str(count) + '\n')
answer.close()
print(count)
