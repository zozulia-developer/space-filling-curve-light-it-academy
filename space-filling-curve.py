import turtle as trtl
from turtle import left, right, forward

trtl.hideturtle()
trtl.color("blue")
trtl.speed(10)
trtl.penup()
trtl.goto(-300, 300)
trtl.pendown()
size = 10


def hilbert(level, angle=90):
    if level == 0:
        return

    right(angle)
    hilbert(level - 1, -angle)
    forward(size)
    left(angle)
    hilbert(level - 1, angle)
    forward(size)
    hilbert(level - 1, angle)
    left(angle)
    forward(size)
    hilbert(level - 1, -angle)
    right(angle)


hilbert(4)

trtl.exitonclick()