n = [int(x) for x in open('input.txt')]
max_0F = max([x for x in n if hex(x)[-2:].lower() == '0f'])
n_output = [(n[i], n[i + 1]) for i in range(0, len(n) - 1) if
            [n[i] % 7, n[i + 1] % 7].count(0) == 1 and (n[i] + n[i + 1]) % max_0F == 0]
print(len(n_output), max(sum(x) for x in n_output))


