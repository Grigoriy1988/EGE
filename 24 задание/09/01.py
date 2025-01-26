s = open('24_4643.txt').readline()
s = s.replace('2','1').replace('B','A')
s =s.replace('11A','*').replace('1',' ').replace('A',' ')
print(max(len(i) for i in s.split()))
# t = {'1':1,"2":2}
# t ={}
# print(len(t))