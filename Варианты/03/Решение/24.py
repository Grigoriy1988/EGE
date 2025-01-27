f = open('24.txt').readline()
# print(f[:40])
f = f.replace('**', ' ').replace('++', ' ').replace('+*', ' ').replace('*+', ' ')
# print(f[:40])
f =f.split()
# print(f[:40])
max_len = 0
for s in f:
    if len(s)> max_len:
        for i in range(len(s)):
            if s[i] not in "+*":
                sub = ''
                for j in range(i,len(s)):
                    sub += s[j]
                    try:
                        if eval(sub) == 0 and s[j] not in '*+':
                            max_len = max(max_len,len(sub))
                    except:
                        pass
print(max_len)


#     if max_res[0] < len (i):
#         try:
#             res = (len(i), eval(i))
#         except:
#             if i[0] in '*+' and i[-1] not in '*+':
#
#                 res = (len(i[1:]), eval(i[1:]))
#             elif i[0] not in '*+' and i[-1] in '*+':
#
#                 res = (len(i[:-1]), eval(i[:-1]))
#             else:
#                 res = (len(i[1:-1]), eval(i[1:-1]))
#         if res[1] == 0 and max_res[0] < res[0]:
#             max_res = res
#
# print(max_res)
