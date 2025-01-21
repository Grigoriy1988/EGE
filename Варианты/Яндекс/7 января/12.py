N = []
for n in range(3, 10000):
    s = '8' + "4" * n
    while '4444' in s or '844' in s or '84' in s:
        if '4444' in s:
            s = s.replace('4444','884',1)
        if '844' in s:
            s = s.replace('844', '488', 1)
        if '84' in s:
            s = s.replace('84', '3343', 1)
    # print(n, len(s))
    N.append(n)
    if len(s) < 20:
        print(n)
        N.clear()
print(min(N) if N else None)


