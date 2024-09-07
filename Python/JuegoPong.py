#juego 1: pong.
#Este juego no usa clases u objetos.

import turtle
import time

ventana=turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

PuntuacionA=0
PuntuacionB=0

#jugador A:
A=turtle.Turtle()
A.speed(0)
A.shape("square")
A.color("white")
A.shapesize(stretch_wid=5, stretch_len=1)  #por default, la forma es un cuadro de 20x20
A.penup()
A.goto(-350, 0)


#jugador B:
B=turtle.Turtle()
B.speed(0)
B.shape("square")
B.color("white")
B.shapesize(stretch_wid=5, stretch_len=1)  #por default, la forma es un cuadro de 20x20
B.penup()
B.goto(350, 0)

#bola:
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)

Ball.dx=0.1
Ball.dy=-0.1

#Contadores
Pen=turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()

Pen.goto(0, 260)
Pen.write("Player A: 0       Player B: 0", align="center", font=("Courier", 24, "normal"))

#funciones:
#las funciones se definen como: def NombreFuncion():
def Aarriba():
    y=A.ycor()  #devuelve Y.
    y+=20
    A.sety(y)

def Aabajo():
    y=A.ycor()  #devuelve Y.
    y-=20
    A.sety(y)

def Barriba():
    y=B.ycor()  #devuelve Y.
    y+=20
    B.sety(y)

def Babajo():
    y=B.ycor()  #devuelve Y.
    y-=20
    B.sety(y)

ventana.listen()
ventana.onkeypress(Aarriba, "w") #se encarga de llamar a la función cuando se presiona w.
ventana.onkeypress(Aabajo, "s")

ventana.onkeypress(Barriba, "Up")
ventana.onkeypress(Babajo, "Down")

#loop:
while True:
    ventana.update()

    #mover la bola:
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)
    
    #al llegar al borde:
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1
    
    if Ball.ycor()<-283:
        Ball.sety(-283)
        Ball.dy*=-1

    if Ball.xcor()>383:
        Ball.goto(0, 0)
        time.sleep(0.5)
        A.goto(-350, 0)
        B.goto(350, 0)
        Ball.dx*=-1
        PuntuacionA+=1
        Pen.clear()
        Pen.write("Player A: {}       Player B: {}".format(PuntuacionA, PuntuacionB), align="center", font=("Courier", 24, "normal"))
    
    if Ball.xcor()<-391:
        Ball.goto(0, 0)
        time.sleep(0.5)
        A.goto(-350, 0)
        B.goto(350, 0)
        Ball.dx*=-1
        PuntuacionB+=1
        Pen.clear()
        Pen.write("Player A: {}       Player B: {}".format(PuntuacionA, PuntuacionB), align="center", font=("Courier", 24, "normal"))
    
    #Colisiones:
    if (Ball.xcor() > 340 and Ball.xcor()<350) and (Ball.ycor() < B.ycor()+40 and Ball.ycor() > B.ycor()-40):
        Ball.setx(340)
        Ball.dx*=-1
    
    if (Ball.xcor() < -340 and Ball.xcor()>-350) and (Ball.ycor() < A.ycor()+40 and Ball.ycor() > A.ycor()-40):
        Ball.setx(-340)
        Ball.dx*=-1




