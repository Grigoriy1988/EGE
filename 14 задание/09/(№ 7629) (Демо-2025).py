for x in range(2030,0,-1):
    a = 7**170 + 7**100 - x
    a_7 = []
    while a> 0:
        a_7.append(a%7)
        a //=7
    if a_7.count(0)== 71:
        print(x)
        break
