from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.goto(-100,200)
        self.color("green")
        self.write(self.l_score,align='center',font=("Courier",60,"normal"))
        self.goto(100,200)
        self.color("red")
        self.write(self.r_score,align='center',font=("Courier",60,"normal"))
        
    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER", align='center', font=("Courier", 50, "normal"))
        self.goto(0,-50)
        if self.l_score>self.r_score:
            self.color("green")
            self.write("Left Player Wins", align='center', font=("Courier", 30, "normal"))
        else:
            self.color("red")
            self.write("Right Player Wins", align='center', font=("Courier", 30, "normal"))
