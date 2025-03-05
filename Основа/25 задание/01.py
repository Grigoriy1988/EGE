# поиск делителей
# d = []
# x = 1_000_000_000
# for i in range(1,x+1):
#     if x % i == 0:
#         d.append(i)
# print(d)

#   все делители лежат до x // 2
#   делители числа x можно разбить на пары a b, такие что a*b = x, перебор можно делать до x**0.5
def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
            # d = d | {i,x // i}
    return sorted(d)
print(div(1_000_000_000_000_000))
