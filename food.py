# made by Jayavant

from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("yellow")
        self.refresh()

    def refresh(self):
        x_random = randint(-280, 280)
        y_random = randint(-280, 280)
        self.goto(x_random, y_random)

