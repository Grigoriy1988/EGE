num = [int(i) for i in open('input.txt')]
print(num)
num_output = [x for x in num if x % 3 == 0 and x % 7 != 0 and  x % 17 != 0 and  x % 19 != 0 and  x% 27 != 0]
print(len(num_output), max(num_output))
