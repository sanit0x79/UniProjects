import turtle

turtle.bgcolor("black")
colours = [
    "red",
    "purple",
    "blue",
    "green",
    "orange",
    "yellow"
]
t = turtle.Turtle()
def spiral(n):
    if n == 0:
        return
    
    t.pencolor(colours[n % 6])
    t.width(n / 100 + 1)
    t.forward(n)
    t.left(59)
    spiral(n - 1)

spiral(210)
turtle.exitonclick()