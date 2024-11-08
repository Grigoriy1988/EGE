from PIL import Image
import itertools
from  random import randint
def point():
    R= randint(250,255)
    G = randint(240,255)
    B = randint(230,255)
    return R,G,B

im = Image.new("RGB", (500, 500), (0, 255, 0))
pixels = im.load()
x, y = im.size
n = 0
k = 54
r, g, b = point()
for i, j in itertools.product(range(x), range(y)):

    if n == k:
        n = 0
        r, g, b = point()
    else:
        n+=1
    pixels[i, j] = r, g, b
im.save('input.png')