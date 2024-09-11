from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your Bet","Which tutrle will win the Race?Enter the Color: ")
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
all_racers=[]
y=-100

def draw_finish_line():
    line=Turtle()
    line.penup()
    line.hideturtle
    line.width(2)
    line.speed(0)
    line.goto(230,250)
    line.pendown()
    line.right(90)
    line.forward(500)
    line.pendown()

draw_finish_line()
for index in range(0,6):
    t=Turtle("turtle")
    t.color(colors[index])
    t.penup()
    t.goto(x=-230,y=y,)
    y+=40
    all_racers.append(t)

if user_bet:
    is_race_on=True

while is_race_on:
    for t in all_racers:
        if t.xcor()>230:
            is_race_on=False
            winner=t.pencolor()
            if winner.lower()==user_bet.lower():
                print(f"You Have Won! The {winner} turtle is the winner")
            else:
                print(f"You Have Lost! The {winner} turtle is the winner")
        rand_dist=random.randint(0,10)
        t.forward(rand_dist)
    
screen.exitonclick()