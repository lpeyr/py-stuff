from turtle import *
import colorsys


def main():
    hue = 0
    num_colors = 380
    pensize(20)
    for i in range(380):
        (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
        color((r, g, b))
        forward(1)
        left(1)
        hue += 0.9/num_colors

    done()


if __name__ == "__main__":
    main()
