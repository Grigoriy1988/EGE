'''
- хотя бы половина чисел набора меньше среднего арифметического пары
- хотя бы четверть чисел набора больше среднего арифметического пары
'''
f = open('26_1079.txt')
n = int(f.readline())
a = [int(i) for i in f]
print(n)
a.sort()
print(a)
count = 0
# print(n // 2)
# print(n - n // 4)
m = a[-1]**2
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            if a[2499] < ((a[i] + a[j]) // 2) < a[3750]:
                count += 1
                m = min(m,(a[i] + a[j]) // 2)
print(count,m)
