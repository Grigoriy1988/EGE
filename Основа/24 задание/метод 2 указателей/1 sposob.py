s = open('input.txt').readline()
s_list = [i for i in s.split('.')]
m = 0
for i in range(0,len(s_list)-1):
    m =max(m, len(s_list[i])+len(s_list[i+1])+1)
print(m)