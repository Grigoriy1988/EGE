# (¬ДЕЛ(х, 84) ∨ ¬ДЕЛ(х, 90)) → ¬ДЕЛ(х, А)


def f(x):
    return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)

for a in range(10000,1,-1):
    if all(f(x) == 1 for x in range(1,1000000)):
        print(a)