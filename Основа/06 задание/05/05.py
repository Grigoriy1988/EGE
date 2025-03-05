from turtle import *
screensize(1000,1000,)
tracer(0)
m = 5
for i in range(10):
    for j in range(3):
        fd(10*m)
        rt(90)
        fd(10*m)
        rt(270)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m,y*m)
        dot(3,"blue")
update()
exitonclick()