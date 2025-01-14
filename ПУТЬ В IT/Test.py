#Способ №1
def f(c, e,flag=False):
    if c == 10:
        flag =True
    if c > e:
        return 0
    if c == e:
        return flag
    if c < e:
        return f(c+1, e,flag) + f(c*2, e,flag)
print(f(1,20))
# Способ №2
a = [0]*21
a[1] = 1
for i in range(1,10):
    if i+1 <= 10:
        a[i+1] +=a[i]
    if i*2 <= 10:
        a[i*2] += a[i]
print(a)
a = [0]*21
a[10] = 14
for i in range(10,20):
    if i+1 <= 20:
        a[i+1] +=a[i]
    if i*2 <= 20:
        a[i*2] += a[i]
print(a)