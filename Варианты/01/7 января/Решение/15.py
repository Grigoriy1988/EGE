from itertools import combinations


# (x∈A)→((x∈B)∨(x∈C))
# B = [101; 143] и C = [144; 199]
def f(x):
    B = 101 <= x <= 143
    C = 144 <= x <= 199
    A = a1 <= x <= a2
    return A <= (B or C)


Ox = [i / 4 for i in range(100 * 4, 199 * 4)]
dx = []  # длинны отрезка а
for a1, a2 in combinations(Ox, 2):
    # print(a1,a2)
    if all(f(x) == 1 for x in Ox):
        # print(a2-a1)
        dx.append(a2 - a1)
print('\n'.join(str(i) for i in dx))
print(max(dx))
