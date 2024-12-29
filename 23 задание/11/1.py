def f (c,e,flag=False):
    if c==8:
        flag = True
    if c==11 or c ==18:
        flag = False
    if c ==e:
        return  flag
    if c>e:
        return 0
    if c < e:
        return f(c+1,e,flag)+f(c+2,e,flag)+f(c*3,e,flag)
print(f(4,23))