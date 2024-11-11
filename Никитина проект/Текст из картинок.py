from PIL import Image
import itertools


f_output = open('output.txt', mode='w', encoding='utf-8')


im_input = Image.open('input.png')
im_code = Image.open('output.png')
pixels = im_input.load()
pixels_code = im_code.load()
x, y = im_input.size
for i, j in itertools.product(range(x), range(y)):
    r, g, b = pixels[i, j]
    r_2, g_2, b_2 = pixels_code[i, j]
    R = r_2 - r if r_2 - r >= 0 else 255 +r_2 - r
    G = g_2 - g if g_2 - g>= 0 else 255 + g_2 - g
    B = b_2 - b if b_2 - b >= 0 else 255 + b_2 - b
    # f_output.write(str(R)+str(G)+str(B) + '\n')
    code = int(('0'* (5-len(bin(R)[2:]))+bin(R)[2:] +'0'*(5-len(bin(G)[2:]))+ bin(G)[2:] + '0'*(5-len(bin(B)[2:]))+bin(B)[2:]),2)
    # print(code)
    if code == 0:
        break
    f_output.write(str(chr(code)))
f_output.close()