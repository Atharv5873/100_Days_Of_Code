from turtle import Turtle,Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)



segments=[]


screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    
    
     


screen.exitonclick()
