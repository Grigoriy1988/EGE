from fnmatch import fnmatch


def div(x):
    return {k for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for k in (i, x // i)}


count = 7
for i in range(65_001, +65_001 + 1000000):
    if fnmatch(str(i),'6*97*5?'):
        d = div(i)
        if len(d)>= 4:
            print(i, sum(x for x in d if x % 2 == 0))
            count -= 1
        if count == 0:
            break