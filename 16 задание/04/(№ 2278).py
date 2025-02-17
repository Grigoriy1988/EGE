'''
F(n) = 2*n*n*n + 1, при n > 25
F(n) = F(n+2) + 2*F(n+3), при n ≤ 25
Определите количество натуральных значений n из отрезка [1; 1000], для которых значение F(n) кратно 11.
'''
def F(n):
    if n> 25:
        return 2*n*n*n + 1
    return F(n+2) + 2*F(n+3)

count = 0
for i in range(1,1001):
    if F(i)%11 == 0:
        count +=1
print(count)