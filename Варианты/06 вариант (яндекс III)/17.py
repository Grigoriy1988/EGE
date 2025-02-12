def f(k):
    return int(k % 100 == 42 and 1000 <= abs(k) <= 9999)
a = [int(i) for i in open('17 (1).txt')]
# print(a)
m = max([i for i in a if i % 100 == 42 and 1000 <= abs(i) <= 9999])
print(m)
output = [(a[i],a[i+1],a[i+2]) for i in range(len(a)-2) if (f(a[i]),f(a[i+1]),f(a[i+2])).count(1) >= 2 and a[i]+a[i+1]+a[i+2] > m]
print(output)
print(len(output),max(sum(i) for i in output))


def f(k):
    return int(k % 100 == 42)
def d(k):
    return int(1000 <= abs(k) <= 9999)

a = [int(i) for i in open('17 (1).txt')]
# print(a)
m = max([i for i in a if i % 100 == 42 and 1000 <= abs(i) <= 9999])
print(m)
output = [(a[i],a[i+1],a[i+2]) for i in range(len(a)-2) if (f(a[i]),f(a[i+1]),f(a[i+2])).count(1) >= 2 and (a[i]+a[i+1]+a[i+2] > m) and (d(a[i]),d(a[i+1]),d(a[i+2])).count(1) >= 2]
print(output)
print(len(output),max(sum(i) for i in output))

