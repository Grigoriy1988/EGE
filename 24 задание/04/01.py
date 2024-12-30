s = open('24_1428.txt').readline()
s = s.replace('XY','X Y').replace('XZ','X Z')
print(max(len(i) for i in s.split()))