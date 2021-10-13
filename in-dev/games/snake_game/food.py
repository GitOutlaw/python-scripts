from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        '''Sets random locaion of food on the screen.'''
        random_x = random.choice(range(-270, 270, 20))
        random_y = random.choice(range(-270, 270, 20))
        self.goto(random_x, random_y)
