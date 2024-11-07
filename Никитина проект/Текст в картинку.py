f_input = open('input.txt', encoding='utf-8')
f_output = open('otput.txt', mode='w')
for line in f_input:
    for sim in line:
        code = bin(ord(sim))[2:]
        code = '0' * (12 - len(code)) + code

        print(code)
