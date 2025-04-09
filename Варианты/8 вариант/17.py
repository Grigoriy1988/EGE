num = [int(i) for i in open('17.txt')]
min_num = min(num)
couples = [(num[i], num[i + 1]) for i in range(len(num) - 1) if num[i] % 117 == min_num or num[i + 1] % 117 == min_num]
print(len(couples), max(sum(i) for i in couples))
