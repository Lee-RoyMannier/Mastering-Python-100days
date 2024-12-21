from turtle import Turtle

class Pad(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x_cord, y_cord)

    def move_up(self):
        self.forward(30)

    def move_down(self):
        self.backward(30)

    def reset_pad(self, x_cord, y_cord):
        self.penup()
        self.goto(x_cord, y_cord)

