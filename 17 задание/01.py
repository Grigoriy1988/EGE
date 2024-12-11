num = [int(i) for i in open('input.txt')]
max_25 = max([i for i in num if abs(i) % 100 == 25])
num_output = [(num[i], num[i + 1], num[i + 2]) for i in range(0, len(num) - 2) if
              [len(str(abs(num[i]))), len(str(abs(num[i + 1]))), len(str(abs(num[i + 2])))].count(4) <= 2 and sum(
                  (num[i], num[i + 1], num[i + 2])) <= max_25]
max_sum = max(sum(x) for x in num_output)
print(len(num_output),max_sum)