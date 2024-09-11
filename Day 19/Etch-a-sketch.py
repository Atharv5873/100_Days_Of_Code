from turtle import Turtle, Screen

def move_forward():
    t.forward(10)
def move_back():
    t.backward(10)
def anti():
    t.left(10)
def clock():
    t.right(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

t = Turtle()
screen = Screen()
t.speed(0)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=anti)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
