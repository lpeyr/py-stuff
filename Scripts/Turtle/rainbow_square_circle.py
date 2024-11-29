from turtle import *
import colorsys


def draw_square(side):

    for i in range(4):
        forward(side)
        left(90)


def main():
    hue = 0
    num_colors = 38
    pensize(5)
    for i in range(38):
        (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
        color((r, g, b))
        draw_square(200)
        hue += 0.9/num_colors
        left(10)
    done()


if __name__ == "__main__":
    main()
