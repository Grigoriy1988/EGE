def f(x,y):
    return (x - 3*y < a) or (y > 400) or (x > 56)
for a in range(400):
    if all(f(x,y)==1 for x in range(0,400) for y in range(0,410)):
        print(a)
