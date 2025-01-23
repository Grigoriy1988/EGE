dig= '0123'
def f(n):
    s = ''
    while n >0:
        s = dig[n % 4] + s
        n //= 4
    return s

for i in range(199,0,-1):

    if len(f(i)) >= 3 and f(i)[-3:] == '123':
        print(i,end='')

