from turtle import *
tracer(0)
# fd - вперед на пиксели
# rt - вправо
# lt - влево
# up() поднять хвост
# down()
# goto() перейти в точку
# dot - точка
# exitonclick() выход по клику
m = 50 # маштаб
for i in range(7):
    rt(90)
    fd(4*m)
    for j in range(2):
        lt(90)
        fd(4*m)
#сетка
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,"blue")

update()
exitonclick()