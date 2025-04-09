def f(c,e,p13=False,p17=False):
    if c == 13:
        p13 = True
    if c == 17:
        p17 = True
    if c > e:
        return 0
    if c < e :
        return f(c+2,e,p13,p17)+f(c+3,e,p13,p17)+f(c+5,e,p13,p17)
    if c == e and ((p13 == True and p17 == False) or (p17 == True and p13 == False)):
        return 1
    else:
        return 0

print(f(5,25))