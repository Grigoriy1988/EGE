file = open('3.txt',encoding='utf-8')
# print(file)
d = dict()
for sting in file:
    grade , name = sting.split()
    if d.get(name,None):
        d[name].append(int(grade))
    else:
        d[name] = [int(grade)]
count = 0
for name , grade in d.items():
    if sum(grade)/len(grade) >=4:
        count+=1
print(count)
