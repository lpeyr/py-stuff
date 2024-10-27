from turtle import *

def triangle1(n):
    up()
    goto(0, 0)
    down()
    for _ in range(3):
        forward(n)
        left(120) # 180 - 60

def triangle2(n):
    up()
    goto(0, 0)
    down()
    for _ in range(3):
        forward(n)
        right(120)

# tests
triangle1(100)
triangle2(100)

exitonclick()