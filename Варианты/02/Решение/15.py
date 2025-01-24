from itertools import combinations


# P = [25, 50] и Q = [37, 60].
#(¬(x∈A)→¬(x∈P))→((x∈A)→(x∈Q))
def f(x):
    p = 25 <= x <= 80
    q = 34 <= x <= 60
    a = a1 <= x <= a2
    return (not(a) <= (not p)) <= (a <= q)


OX = [i / 4 for i in range(20 * 4, 80 * 4)]
dx = []
for a1, a2 in combinations(OX, 2):
    if all(f(x) == 1 for x in OX):
        # print(a2 - a1)
        dx.append(a2 - a1)
print('\n'.join(str(i) for i in dx))
print(max(dx))
