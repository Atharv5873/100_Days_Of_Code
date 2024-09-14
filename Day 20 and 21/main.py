from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
segments=[]


screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.04)
    snake.move()

    if snake.head.distance(food) <15:
        food.refresh()
        snake.extends()
        scoreboard.increase_score()

    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        scoreboard.game_over()
        game_is_on=False
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            game_is_on=False
     


screen.exitonclick()
