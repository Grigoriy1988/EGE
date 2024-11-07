from PIL import Image
import itertools

im_input = Image.open('input.png')
pixels = im_input.load()
x, y = im_input.size

f_input = open('input.txt', encoding='utf-8')

list_code = []
for line in f_input:
    for sim in line:
        code = bin(ord(sim))[2:]
        code = '0' * (12 - len(code)) + code
        list_code.append(code)

n = 0
for i, j in itertools.product(range(x), range(y)):
    r, g, b = pixels[i, j]
    if n < len(list_code):
        r = (r + int(list_code[n][0:4], 2)) % 255
        g = (g + int(list_code[n][4:8], 2)) % 255
        b = (b + int(list_code[n][8:],2)) % 255
    n += 1
    pixels[i, j] = r, g, b
im_input.save('output.png')
f_input.close()
