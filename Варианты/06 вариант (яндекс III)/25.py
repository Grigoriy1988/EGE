from fnmatch import *
for i in range(0,10**10+1,96437):
    if fnmatch(str(i),'7?2*4??9?'):
        print(f'{i}\t{i//96437}')

