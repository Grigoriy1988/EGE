# ДЕЛ(A, 9) ∧ (ДЕЛ(280, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(730, x)))
def DEL(x, a):
    return (a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))


for a in range(1, 1000):
    if all(DEL(x, a) == 1 for x in range(1, 1000000)):
        print(a)
