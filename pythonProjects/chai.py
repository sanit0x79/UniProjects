from turtle import *
from random import choice

def chai(dist):
    if dist < 5:
        return

    forward(dist)
    left(90)
    forward(dist / 2)
    right(90)

    right(90)
    forward(dist)
    left(90)

    left(90)
    forward(dist / 2.0)
    right(90)
    backward(dist)

chai(100)
exitonclick()
