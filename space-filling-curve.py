import turtle as trtl
from turtle import left, right, forward

trtl.hideturtle()
trtl.color("blue")
trtl.speed(10)
trtl.penup()
trtl.goto(-430, 360)
trtl.pendown()
size = 12


def hilbert_curve(level, angle=90):
    if level == 0:
        return

    right(angle)
    hilbert_curve(level - 1, -angle)
    forward(size)
    left(angle)
    hilbert_curve(level - 1, angle)
    forward(size)
    hilbert_curve(level - 1, angle)
    left(angle)
    forward(size)
    hilbert_curve(level - 1, -angle)
    right(angle)


hilbert_curve(5)

trtl.exitonclick()