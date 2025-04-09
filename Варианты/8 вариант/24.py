s = open('24.txt').readline()
s = s.replace("C",'B')
count = 1
while "BBA" * count in s:
    count += 1
print((count-1) * 3)