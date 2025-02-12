def print_boxed(arr):
    arr_stringified = [str(element) for element in arr]
    mid = ' | '.join(arr_stringified)
    bar = '-' * (2 + len(mid))
    print(' ' + bar + ' ')
    print('| ' + mid + ' |')
    print(' ' + bar + ' ')


def print_simple(arr):
    arr_stringified = [str(element) for element in arr]
    print(', '.join(arr_stringified))


formatting = 'boxed'
if formatting == 'boxed':
    print_formatted = print_boxed
else:
    print_formatted = print_simple

# Дальше в программе можно использовать print_formatted повсюду
print_formatted([1, 1, 2, 3, 5, 8, 13, 21])
print_formatted([1, 2, 4, 8, 16, 32, 64, 128])
print_formatted(['abc', 'def', 'ghi'])