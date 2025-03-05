def f(c, e, command=''):
    if c > e:
        return 0
    if c == e and command.count('*') == 1 :
        return 1
    if c == e and command.count('*') != 1 :
        return 0
    if '*' not in command:

        return f(c + 1, e, command + '+') + f(c + 2, e, command + '+') + f(c * 2, e, command + '*')
    else:
        return f(c + 1, e, command + '+') + f(c + 2, e, command + '+')
print(f(2,12))
