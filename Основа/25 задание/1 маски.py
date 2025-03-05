# from fnmatch import *
# for x in range(0,10**9,17):
#     if fnmatch(str(x),'23?456?89'):
#         print(x,x//17)

for a in range(10):
    for b in range(10):
        x = int(f'23{a}456{b}89')
        if  x% 17==0:
            print(x, x // 17)
            