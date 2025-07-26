from turtle import *
from colorsys import *

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.title("Turtle as Cursor")

screen.getcanvas().config(cursor="none")

flower = Turtle()
flower.hideturtle()
flower.speed(0)
flower.pensize(1)

hue = 0.0

def draw_flower(x, y):
    global hue
    flower.clear()
    flower.penup()
    flower.goto(x, y)
    flower.pendown()

    for i in range(12):
        r, g, b = hsv_to_rgb(hue % 1.0, 1, 1)
        flower.color(r, g, b)
        flower.circle(15, 60)
        flower.left(100)
        hue += 0.01

    screen.update()

def on_mouse_move(x, y):
    draw_flower(x - screen.window_width() // 2, screen.window_height() // 2 - y)

canvas = screen.getcanvas()
canvas.bind('<Motion>', lambda e: on_mouse_move(e.x, e.y))

screen.listen()
done()
