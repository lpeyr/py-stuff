from turtle import *


def draw_square(side):
    color("black", "white")

    begin_fill()

    for i in range(4):
        forward(side)
        left(90)

    end_fill()


def main():
    color("black", "white")

    begin_fill()

    for i in range(38):
        draw_square(200)
        left(10)

    end_fill()
    done()


if __name__ == "__main__":
    main()
