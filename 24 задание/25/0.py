s = open('24_5171.txt').readline()
i = 1
while 'CA'*i in s:
    print(i)
    i+=1
if 'CA'*27 + "C" in s:
    print(len('CA'*27 + "C"))
else:
    print(len('CA'*27))