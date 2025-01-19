def square(x):
    return x * x


def factorial(a):
    f = a
    for i in range(2, a):
        f *= i
    return f


def apply_function(fn, a): return fn(a)


result = apply_function(square, 5)
print(result)
result = apply_function(factorial, 5)
print(result)

