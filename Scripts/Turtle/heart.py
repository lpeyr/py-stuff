from turtle import *


speed(100)


def curve():
    for i in range(200):

        # Defining step by step curve motion
        right(1)
        forward(1)

# Defining method to draw a full heart


def heart():
    right(90)
    pensize(5)
    # Set the fill color to red
    fillcolor('red')

    # Start filling the color
    begin_fill()

    # Draw the left line
    left(140)
    forward(113)

    # Draw the left curve
    curve()
    left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    forward(112)

    # Ending the filling of the color
    end_fill()


heart()

exitonclick()
