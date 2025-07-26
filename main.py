from turtle import *
from colorsys import *

# Setup
penup()
setposition(50, -50)
pendown()
speed(0)
bgcolor('black')
pensize(2)

n = 100
h = 0

for i in range(120):
    for j in range(4):
        r, g, b = hsv_to_rgb(h, 1, 1)
        color(r, g, b)
        h += 0.003
        circle(40 + j * 5, 90)
        forward(250)
        left(90)
    right(10)

hideturtle()
done()
