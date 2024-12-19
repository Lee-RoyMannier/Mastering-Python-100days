from turtle import Turtle
from random import randint

class TurtleModel(Turtle):
    def __init__(self, xcor, ycor, color):
        Turtle.__init__(self)
        self.shape('turtle')
        self.color(color)
        self.penup()
        self.goto(xcor, ycor)

    def run(self):
        self.forward(randint(0, 10))