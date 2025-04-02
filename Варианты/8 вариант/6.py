x,y = 0,0
for i in range(8):
    x+=30
    y+=10

    x += 50
    y -= 30

    x -= 40
    y += 50
print(x,y)
r = (x**2+y**2)**0.5
print(r)

