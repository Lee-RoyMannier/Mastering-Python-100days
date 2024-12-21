from turtle import Turtle

class Pad(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(2,5)
        self.penup()
        self.goto(x_cord, y_cord)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)