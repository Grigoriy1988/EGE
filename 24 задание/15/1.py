#s = open('24_4113.txt').readline()
# способ замен: не работает DBBBDDDD
# s = 'DBBBDDDD'
# s = s.replace('BB','*').replace('DD','*')
# s =s.replace('A',' ').replace('D',' ').replace('B',' ')
# print(s.split())
# print(max(len(i) for i in s.split()))
s = open('24_4113.txt').readline()
#s = 'DBBBDDDD'
m=[0]*len(s)
for i in range(1,len(s)):
    if s[i-1]+ s[i] == "BB" or s[i-1]+ s[i] == "DD":
        m[i] = m[i-2]+1
print(max(m))
