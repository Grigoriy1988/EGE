f = open('24.txt').readline()
for a in '*+-':
    for b in '*+-':
        f = f.replace(a+b,' ')
f = f.replace('B',' ').replace('C',' ').replace('D',' ').replace('*',' ').replace("A"," A").split()
f = [i for i in f if 'A' in i and len(i)>1 and i[1] not in '+-*']
max_sum = (0,0)
for i in f:
    try:
        a = eval(i[1:])
        l = len(i[1:])
        if l > max_sum[0] or (l == max_sum[0] and a > max_sum[1]):
            max_sum = (l,a)
            print(f'{i} = {a} длинна {l}')
    except:
        pass
print(max_sum)

