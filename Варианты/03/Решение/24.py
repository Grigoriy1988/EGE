f = open('24.txt').readline()
f = f.replace('**', ' ').replace('++', ' ').replace('+*', ' ').replace('*+', ' ')
f =f.split()
max_res = (0,0)
for i in f:
    if max_res[0] < len (i):
        try:
            res = (len(i), eval(i))
        except:
            if i[0] in '*+' and i[-1] not in '*+':

                res = (len(i[1:]), eval(i[1:]))
            elif i[0] not in '*+' and i[-1] in '*+':

                res = (len(i[:-1]), eval(i[:-1]))
            else:
                res = (len(i[1:-1]), eval(i[1:-1]))
        if res[1] == 0 and max_res[0] < res[0]:
            max_res = res

print(max_res)


print(eval("4+5"))