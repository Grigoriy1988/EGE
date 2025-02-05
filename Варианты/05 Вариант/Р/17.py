a = [int(i) for i in open('17.txt')]
m = min(a)
b = [[a[i],a[i+1]] for i in range(len(a)-1) if a[i] % 77 + a[i+1]% 77 == m]
print(len(b), max(sum(i) for i in b))