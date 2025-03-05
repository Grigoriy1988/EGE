n = [int(x) for x in open('input.txt')]
max_8 = max([x for x in n if str(abs(x))[0] == '8'])
n_output = [(n[i], n[i + 1], n[i + 2]) for i in range(0, len(n) - 3) if
            [str(abs(n[i]))[0], str(abs(n[i + 1]))[0], str(abs(n[i + 2]))[0]].count('6') <= 1 and n[i] + n[i + 1] + n[
                i + 2] >= max_8]
min_s = min(sum(x) for x in n_output)
print(len(n_output),min_s)

