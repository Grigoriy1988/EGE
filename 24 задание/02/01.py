# Метод двух указателей
s = open('24_2426.txt').readline()
l = 0
m = 0
for r in range(len(s)):
    if s[r] in 'ABC':
        l = r + 1
    if s[r] in '123':
        m = max(m,r - l + 1)
print(m)
