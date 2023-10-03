from turtle import *
from random import choice
def rwalk(N):
    if N == 0:
        return
    
    direction = choice(["left", "right"])

    if direction == "left":
        left(45)
    else:
        right(45)
    forward(20)
    rwalk (N - 1)
"""
    if direction == "left":
        left(45)
        forward(20)
        rwalk(N - 1)
    else:
        right(45)
        forward(20)
        rwalk(N - 1)
"""
def poly(runs, TOTAL_SIDES):
    """Teken een polygoon met runs/TOTAL_SIDES
    """
    if runs == 0:
        return  # klaar
    else:
        forward(100)
        left(360 / TOTAL_SIDES)
        poly(runs - 1, TOTAL_SIDES)


rwalk(200)
exitonclick()