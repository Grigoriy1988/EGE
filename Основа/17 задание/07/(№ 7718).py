def f(a, b, c, d, m):
    if [a % 2, b % 2, c % 2, d % 2].count(0) % 2 != 0 and a < m and b < m and c < m and d < m:
        return 1
    return 0


n = [int(x) for x in open('input.txt')]
max_1 = max([x for x in n if x % 10 == 1])
n_output = [(n[i], n[i + 1], n[i + 2], n[i + 3]) for i in range(0, len(n) - 3) if
            f(n[i], n[i + 1], n[i + 2], n[i + 3], max_1)]
min_s = min(sum(x) for x in n_output)
print(len(n_output), min_s)
