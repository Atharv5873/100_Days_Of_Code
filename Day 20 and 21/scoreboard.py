from turtle import Turtle
ALIGNMENT ='center'
FONT=("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=(FONT))
        