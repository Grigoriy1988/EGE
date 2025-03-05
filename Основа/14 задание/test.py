def f(a):
    result = []
    while a >0:
        result.append(a%3)
        a //=3
    return result
x = 9**12+3**241 - 12
x_3 = f(x)
print(sum(int(i) for i in str(x)))
print(x_3)
print(x_3.count(1),x_3.count(2))
print(sum(x_3))
