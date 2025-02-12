# (¬ДЕЛ(x,A)∧(x∈B))→¬ДЕЛ(x,13)


def f(x):
    return ((x % a != 0) and (132 <= x <= 150)) <= (x % 13 != 0)

for a in range(1,10000):
    if all(f(x) == 1 for x in range(1,1000000)):
        print(a)