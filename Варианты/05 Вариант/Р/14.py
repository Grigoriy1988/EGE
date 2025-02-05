x = 4 **644 + 4 ** 322 + 16**35 - 64**3
x_4 = []
while x >0:
    x_4.append(x % 4)
    x//=4
print(x_4.count(3))
