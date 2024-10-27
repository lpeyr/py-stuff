from turtle import *

colors = ["#000077", "white", "red"]

def rectangle(color):
    begin_fill()
    fillcolor(color)
    for _ in range(2):
        down()
        forward(100)
        left(90)
        forward(200)
        left(90)
    end_fill()

for c in colors:
    rectangle(c)
    up()
    forward(100)
    down()

exitonclick()