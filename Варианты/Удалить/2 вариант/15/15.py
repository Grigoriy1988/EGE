# (2y>5x)∨(xy<a)∨(x≥22)
def f(x, y):
    return (2 * y > 5 * x) or (x * y < a) or (x >= 22)


for a in range(0, 1800):
    if all(f(x, y) == 1 for x in range(0, 23) for y in range(0, 100)):
        print(a)
