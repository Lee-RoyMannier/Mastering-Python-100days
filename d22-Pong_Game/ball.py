from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.start()

    def start(self):
        self.penup()
        self.goto(0, 0)

