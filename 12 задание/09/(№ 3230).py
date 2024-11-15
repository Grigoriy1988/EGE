min_k = []

for k in range(81,100):
    s = '1'*k

    while '111' in s:
        s = s.replace('111','2',1)
        s = s.replace('2222','1',1)
    print(k,s)
    min_k.append((s.count('1'),k))
print(min_k)