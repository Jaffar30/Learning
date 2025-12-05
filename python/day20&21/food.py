from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("green")
        self.speed("fastest")
        self.update_loc()

    def update_loc(self):
        self.goto(random.randint(-270 , 270) , random.randint(-270 , 270))  