f = open('26_2652.txt')
n = int(f.readline())
tovar = dict()
for i in range(n):
    a = int(f.readline())
    if tovar.get(a,0):
        tovar[a]+=1
    else:
        tovar[a] = 1

print(len(tovar),tovar[max(tovar, key=tovar.get)] )

