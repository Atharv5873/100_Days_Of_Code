from turtle import Turtle,Screen
import random
from random import choice
from random import choice
def draw_square(a):
    for i in range(4):
        t.right(90);
        t.forward(a);
def draw_dashed_line(a):
    for i in range(50):
        t.forward(a)
        t.penup()
        t.forward(a)
        t.pendown()
def draw_shape(sides,length):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor((r,g,b))
    for i in range(sides):
        t.forward(length)
        t.right(360/sides)
def draw_all_shapes():
    for side in range(3,11):
        draw_shape(side,100)
def draw_random_walk():
    choice=[90,180,270,0]
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.pencolor((r,g,b))
        t.forward(40)
        t.setheading(random.choice(choice))
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor((r,g,b))
def draw_spirograph(size):
    for i in range(int(360/size)):
        random_color()
        t.circle(80)
        t.setheading(t.heading()+size)
t=Turtle()
screen=Screen()
screen.colormode(255)
t.shape('arrow')
t.speed(0)




draw_spirograph(1)
screen.exitonclick()    




