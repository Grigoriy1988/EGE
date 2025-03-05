nun = [int(x) for x in open('input.txt')]
max_25 = max([int(x) for x in nun if abs(x) % 100 == 25])
nun_output = [(nun[i], nun[i + 1], nun[i + 2])for i in range(0, len(nun) - 2) if
              [len(str(abs(nun[i]))), len(str(abs(nun[i + 1]))), len(str(abs(nun[i + 2])))].count(4) <= 2 and sum(
                  (nun[i], nun[i + 1], nun[i + 2])) <= max_25]
max_summ = max(sum(x) for x in nun_output)
print(len(nun_output),max_summ)