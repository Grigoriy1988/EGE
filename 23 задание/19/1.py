answer = set()

def f(c,step=0):
    if step==15:
        answer.add(c)
    else:
        f(c*2,step+1)
        f(c*2+1,step+1)

f(1)
print(len(answer))