from turtle import Turtle
import random
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(0.7,0.7)
        self.color(random.choice(colors))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
