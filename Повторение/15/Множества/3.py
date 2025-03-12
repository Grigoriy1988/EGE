# 7559
s= 'ДЕЛ(х, 33) → (¬ДЕЛ(х, A) → ¬ДЕЛ(х, 242))'
def f(x):
    return (x % 33 == 0) <= ((x % A != 0) <= (x %  242 != 0))
res = []
for A in range(1,1000):
    if all(f(x) == 1 for x in range(1000)):
        res.append(A)
print(max(res))