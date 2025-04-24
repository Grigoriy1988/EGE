def f(x):
  return len({k for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for k in (i, x // i)})



a = [14, 6, 5, 8, 4]
res = []
for i in a:
    res.append([f(i),i])
res.sort(key=lambda x:x[0])

a1 = [x[1] for x in res]

print(a)
print(a1)

