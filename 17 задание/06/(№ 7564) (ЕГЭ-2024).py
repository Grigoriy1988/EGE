def f(a):
    if abs(a) % 10 == 7 and 1000 <= abs(a) <= 9999:
        return 1
    return 0


num = [int(x) for x in open('input.txt')]
max_7 = max([x for x in num if abs(x) % 10 == 7 and 1000 <= abs(x) <= 9999])
num_output = [(num[i], num[i + 1], num[i + 2]) for i in range(0, len(num) - 2) if
              ([f(num[i]), f(num[i + 1]), f(num[i + 2])].count(1) >= 2) and (num[i]+ num[i + 1]+ num[i + 2]) > max_7]
max_s  = max(sum(x) for x in num_output)
print(len(num_output),max_s)

