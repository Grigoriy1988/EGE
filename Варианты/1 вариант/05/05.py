def суума(a):
    even = sum(int(i) for i in str(a) if int(i) % 2 == 0)
    odd = sum(int(i) for i in str(a) if int(i) % 2 == 1)
    return int(str(min(even,odd))+str(max(even,odd)))
count= 0
for N in range(1000000000, 10000000000):
    R = суума(N)
    if R == 3843:
        count +=1

print(count)
