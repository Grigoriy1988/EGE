from turtle import *
tracer(0)
screensize(10000,10000)
# fd(x) - вперед на х пикселей
# rt(y) - вправо на y градусов
# lt(y) - влево на y градусов
# up() - поднять хвост
# down() - опустить хвост
# goto(x,y) - перейти в точку
# dot(размер, цвет) - точка
# exitonclick() - выход
m = 10
for i in range(7):
    goto(xcor() + 6 * m,ycor() - 9 * m)
    goto(xcor() - 6 * m, ycor() +2 * m)
    goto(xcor() + 12 * m, ycor() +3 * m)

up()
for x in range(-20,20):
    for y in range(-20,20):
       goto(x*m,y*m)
       dot(3,'blue')
update()
# input()
exitonclick()