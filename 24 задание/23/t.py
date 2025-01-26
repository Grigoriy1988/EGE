s = open('24_11954.txt').readline().split('Y')
for a in s:
    if a.count('X') >= 500:
        for i in range(len(a)):
            if a[i:].count('X') >= 500:
                str_a = a[i:]
                print(len(a[i:]))
            str_a = str_a[::-1]
        for i in range(len(str_a)):
            if str_a[i:].count('X') >= 500:
                print(len(str_a[i:]))
