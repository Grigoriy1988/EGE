# ДЕЛ(х, 33) → (¬ДЕЛ(х, A) → ¬ДЕЛ(х, 242))
def f(x):
    return (x % 33 == 0) <= ((x % a != 0) <= (x % 242 != 0))
for a in range(1,1000):
    if all(f(x) == 1 for x in range(1,100000)):
        print(a)