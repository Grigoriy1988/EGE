from fnmatch import fnmatch
for x in range(0, 10 ** 9 + 1, 42):
    if fnmatch(str(x), '48*15*0'):
        print(f"{x}\t{x // 42}")