s = '2'*80
while '222' in s or '333' in s:
    if '222' in s:
        s = s.replace('222','33',1)
    else:
        s = s.replace('333','22',1)
print(s)