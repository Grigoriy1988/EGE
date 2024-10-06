from turtle import *
screensize(10000,10000,)
tracer(0)
m = 25
for i in range(7):
    goto(xcor() + 6*m,ycor()-9*m)
    goto(xcor() -6 * m, ycor() +2 * m)
    goto(xcor() + 12 * m, ycor() +3 * m)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,"blue")
update()
exitonclick()
