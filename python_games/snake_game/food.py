from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup() # För att den inte skall rita något.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('purple')
        self.speed('fastest') # Hindra "ghosting" när den skapas centralt och sedan flyttas ut.
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)