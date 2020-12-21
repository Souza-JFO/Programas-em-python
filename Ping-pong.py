import turtle

# Base
class Box(turtle.Turtle):
    def __init__(self,x,y,w,h):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red","gray")
        self.penup()
        self.goto(x,y)
        self.shapesize(w,h)
    # controle de personagem
    def up(self):
        self.sety(self.ycor() + (self.ycor()<220) * (30))
    def down(self):
        self.sety(self.ycor() - (self.ycor()>-220) * (30))
    # placar
    def draw(self):
        self.write("Jogador: {}      Rival: {} ".format(self.pts,self.ptsPc),
                   font=("Arial",40,"normal"),align="center")

#Placar
class Scorre(Box):
    def __init__(self,x,y,w,h):
        Box.__init__(self,x,y,w,h)
        self.goto(x,y)
        self.pts =0
        self.ptsPc=0
        self.hideturtle()
        self.draw()
    
        
# Bola

class Ball(Box):
    def __init__(self,x,y,w,h):
        Box.__init__(self,x,y,w,h)
        self.shape("circle")
        self.color("blue")
       #contantes importantes para movimentação da bola
        self.rivaly = 0
        self.hmy=0
        self.ballx = 0
        self.bally = 0
        self.vx = 0.5
        self.vy = 0.5

    def update(self):
        self.ballx += self.vx
        self.bally += self.vy
        ball.goto(self.ballx,self.bally)
        rival.goto(rival.xcor(),self.rivaly)
        #jogar só://human.goto(human.xcor(),self.hmy)
        # coodernadas x da bola(direita e esquerda)
        if self.ballx >= rival.xcor() - 30 and self.bally < rival.ycor() +50 and self.bally > rival.ycor() -50:
            self.vx *= -1
        if self.ballx <= human.xcor() + 30 and self.bally < human.ycor() +50 and self.bally > human.ycor() -50:
            self.vx *= -1
        elif self.ballx < -350:
            self.vx *= -1
            scorre.ptsPc +=1
            scorre.clear()
            scorre.draw()
        if ball.xcor()==human.xcor() and ball.ycor() == human.xcor():
            self.vx*=-1
            
        elif self.ballx > 350:
            self.vx *= -1
            scorre.pts +=1
            scorre.clear()
            scorre.draw()
        
        # coodernadas y da bola(cima e baixo)    
        if self.bally >= 280 or self.bally <= -280:
            self.vy *= -1
        # movimentação automatica do humano
        if self.ballx < 20:
            if human.ycor() < self.bally and self.hmy < 220:
                self.hmy += 1
            if human.ycor() > self.bally and self.hmy > -220:
                self.hmy -= 1
        
        # movimentação do rival automatico
        if self.ballx > 20:
            if rival.ycor() < self.bally and self.rivaly < 220:
                self.rivaly += 0.7
            if rival.ycor() > self.bally and self.rivaly > -220:
                self.rivaly -= 0.7


# Participantes
human=Box(-350,0,8,1)
rival=Box(350,1,8,1)
# Objeto
ball=Ball(0,0,2,2)

#placar//posição
scorre = Scorre(0,230,10,10)

#tela
win= turtle.Screen()
win.title("Ping-pong 1.0")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#Controles
win.listen()
win.onkeypress(human.up,"Up")
win.onkeypress(human.down,"Down")


# Laço do jogo
while True:
    win.update()
    ball.update()
    if scorre.ptsPc == 5 or scorre.pts == 5:
        break
    
