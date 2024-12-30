s = open('24_2420.txt').readline()
s=s.replace('C',' ').replace('D',' ').split()
print(max(len(i) for i in s))
