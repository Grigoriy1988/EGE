def s(a):
    return sum(int(i) for i in str(abs(a))) % 5 == 0

num = [int(i) for i in open('17.txt')]
max_3 = max([x for x in num if 100<=x<=999])
num_output = [(num[i], num[i + 1]) for i in range(0, len(num) - 1) if (s(num[i]) and not s(num[i+1]) or s(num[i+1]) and not s(num[i])) and abs(num[i]**2 -num[i+1]**2)>=max_3 ** 3]
sum_n = [sum(i) for i in num_output]
print(len(num_output),max(sum_n))