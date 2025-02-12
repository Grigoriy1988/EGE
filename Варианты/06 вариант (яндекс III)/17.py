def f(k):
    return int(k % 100 == 42 and 1000 <= abs(k) <= 9999)
a = [int(i) for i in open('17.txt')]
# print(a)
m = max([i for i in a if i % 100 == 42 and 1000 <= i <= 9999])
print(m)
output = [(a[i],a[i+1],a[i+2]) for i in range(len(a)-2) if (f(a[i]),f(a[i+1]),f(a[i+2])).count(1) >= 2 and a[i]+a[i+1]+a[i+2] > m]
print(output)
print(len(output))

