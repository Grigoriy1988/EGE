from time import time
start_time = time()
def F14(n):
    a = '0123456789abcde'
    s=''
    while n>0:
        s+=a[n%14]
        n//=14
    return s[::-1]
print(F14(855_000_000))
l=0
for q1 in '12345678':
    for q2 in '0123456789abcd':
        for q3 in '0123456789abcd':
            for q4 in '0123456789abcd':
                for q5 in '0123456789abcd':
                    for q6 in '0123456789abcd':
                        for q7 in '0123456789abcd':
                            for q8 in '0123456789abcd':
                                s= q1+q2+q3+q4+q5+q6+q7+q8
                                if (int(s,14))<738_000_000:l+=1
print(l)
end_time = time()
print(end_time - start_time)