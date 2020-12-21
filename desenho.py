import turtle
import random


def color_size(t, l):
    color = '#444C38'  
    if l <= 8:  
        color = '#00FF00' if random.uniform(0, 10) > 3.5 else '#FF69B4'
    elif l <= 30:  
        color = '#006600'
    t.pencolor(color)
    t.pensize(l / 10)


def angle():
    return random.uniform(10, 40)


def new_length(l):
    return l + random.gauss(-5, 1)


def tree(t, l, tree_on_middle=False):
    if l <= 0:
        return

    angle_r = angle()
    angle_l = angle()
    angle_m = (angle_l + angle_r) / 2

    color_size(t, l)
    t.forward(l)  

    t.left(angle_l)
    tree(t, new_length(l), tree_on_middle)

    t.right(angle_m)
    if tree_on_middle:
        tree(t, new_length(l), tree_on_middle)  

    t.right(angle_m)
    tree(t, new_length(l), tree_on_middle)  

    t.left(angle_r)  

    color_size(t, l)
    t.backward(l)  


my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)
my_turtle.left(90)
my_turtle.penup()
my_turtle.backward(200)
my_turtle.pendown()

tree(my_turtle, 40, False)

with open('./tree.ps', 'wb') as pdf:
    pdf.write(turtle.Screen().getcanvas().postscript().encode('utf-8'))

turtle.Screen().exitonclick()
