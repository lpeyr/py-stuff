from turtle import *
import colorsys

title("Bonus - Défi de la spirale")

def triangle(n):
    begin_fill()
    fillcolor("red")
    down()
    for _ in range(3):
        forward(n)
        left(120)
    end_fill()

def carre(n):
    down()
    begin_fill()
    fillcolor("green")
    for _ in range(4):
        forward(n)
        left(90)
    end_fill()

t = 1
speed(100)
for _ in range(75):
    carre(t)
    up()
    forward(t)
    triangle(t)
    up()
    forward(t)
    left(15)
    t += 1

exitonclick()