num = [int(i) for i in open('input.txt')]
num_output = [(num[i], num[i + 1]) for i in range(0, len(num) - 1) if
              (abs(num[i]) % 7 == 0 or abs(num[i + 1]) % 7 == 0) and abs((num[i] + num[i + 1])) % 100 == 19]
s = [sum(a) for a in num_output]
print(len(num_output), max(s))
