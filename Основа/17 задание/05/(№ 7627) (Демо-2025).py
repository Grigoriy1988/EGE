num = [int(x) for x in open('input.txt')]
num_output = [(num[i], num[i+1]) for i in range(0,len(num)-1) if [num[i]% 16,num[i+1]% 16].count(min(num)) >= 1]
print(len(num_output),max(sum(x) for x in num_output))

