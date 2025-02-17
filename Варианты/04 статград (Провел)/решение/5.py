dig = '012'
def r(x):
    s = ''
    N = x
    while x > 0:
        s = dig[x % 3] + s
        x //= 3
    # print(s)
    for i in range(len(s)):
        if s[i] == "0":
            s = s[:i] + '2' + s[i + 1:]
        elif s[i] == "2":
            s = s[:i] + '0' + s[i + 1:]

    return abs(N - int(s, 3))



for n in range(3323600, 10000000):
    if r(n) == 1864246:
        print(n)
        break

