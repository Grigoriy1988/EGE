def roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / 2 * a
    return (-b + d ** 0.5) / 2 * a, (-b - d ** 0.5) / 2 * a

print(roots(1,2,1))
print(roots(4,2,1))
print(roots(1,-4,3))

