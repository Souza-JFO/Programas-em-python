from turtle import *
color('red', 'yellow')
begin_fill()

win=Screen()
win.bgcolor('black')
win.setup(width=600,height=400)
win.title('Teste de desenho')

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

