answer = set()
def f(c,step=0):
    if step==8:
        if 1000<=c<=1024:
            answer.add(c)
    else:
        f(c+1,step+1)
        f(c+5,step+1)
        f(c*3,step+1)
f(1)
print(len(answer))