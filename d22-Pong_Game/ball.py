from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.start()
        self.move_speed_x = 10
        self.move_speed_y = 10
        self.speed = 0.1


    def start(self):
        self.penup()
        self.goto(0, 0)

    def move(self):
        x_cord = (self.xcor() + self.move_speed_x)
        y_cord = (self.ycor() + self.move_speed_y)
        self.goto(x_cord, y_cord)

    def bounce_y(self):
        self.move_speed_y *= -1

    def bounce_x(self):
        self.move_speed_x *= -1
        self.speed *= 0.9


    def restart(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()


