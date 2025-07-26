from turtle import *
from colorsys import *

bgcolor('black')
speed(0)
pensize(2)
hideturtle()
penup()
setposition(50, -50)
pendown()

h = 0.0 
num_shapes = 120
sides = 4

for i in range(num_shapes):
    for j in range(sides):
        r, g, b = hsv_to_rgb(h % 1.0, 1, 1)
        color(r, g, b)
        h += 0.005
        circle(40 + j * 5, 90)
        forward(250)
        left(90)
    right(10)

done()
