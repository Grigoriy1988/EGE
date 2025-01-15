def filter_and_apply(a,fa,fn):
    a = list(filter(fa,a))
    a = list(map(fn, a))
    return a


numbers = [1, 2, 3, 4, 5, 6]
result = filter_and_apply(numbers, lambda x: x % 2 == 0, lambda x: x * x)
print(result)

result = filter_and_apply(numbers, lambda x: x % 2 != 0, lambda x: 2 * x)
print(result)

