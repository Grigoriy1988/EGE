def f(curr, end):
    if curr > end or curr == 4:
        return 0
    if curr == end:
        return 1
    if curr <end:
        return f(curr + 1, end) + f(curr * 2, end)
print(f(2, 16))
# не прох. через 4
