from turtle import *
from math import sqrt

def triangle():
    begin_fill()
    for _ in range(3):
        fillcolor("black")
        forward(100)
        left(120)
    end_fill()

triangle()
up()
forward(100)
down()
triangle()
up()
forward(-100)
left(60)
forward(100)
right(60)
down()
triangle()
exitonclick()