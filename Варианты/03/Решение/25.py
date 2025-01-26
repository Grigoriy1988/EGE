def div(a):
    return [k for i in range(2, int(a**0.5)+1) if a % i == 0 for k in (i, a // i)]

x = 700001
count = 0
while count <5:
    div_list = div(x)
    div_list_7 = sorted([i for i in div_list if i % 10 == 7 and i != 7])
    if div_list_7:
        count +=1
        print(f'{x}\t{div_list_7[0]}')
    x +=1