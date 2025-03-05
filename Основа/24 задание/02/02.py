s = open('24_2426.txt').readline()
s = s.replace('A'," ").replace('B'," ").replace('C',' ').split()
print(max(len(i) for i in s))
