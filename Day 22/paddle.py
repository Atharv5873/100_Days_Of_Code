from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(5,1)
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
        y=self.ycor()
        if y<240:
            self.goto(350,y+20)
    def go_down(self):
        y=self.ycor()
        if y>-240:
            self.goto(350,y-20)
