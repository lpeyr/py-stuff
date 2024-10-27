from turtle import *

def carre(n):
    color("red")
    for _ in range(4):
        forward(n)
        left(90)


def ligne_de_carres(a, n):
    for _ in range(n):
        carre(a)
        up()
        forward(a+10)
        down()

# tests
ligne_de_carres(100, 5)

exitonclick()