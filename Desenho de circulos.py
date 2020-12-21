from turtle import *
bgcolor('black')
pensize(2)
speed(0)

for cor in range(6):
    for colours in ['red','magenta','green','blue','gray','yellow','white']:
        color(colours)
        circle(100)
        left(10)

hideturtle()
