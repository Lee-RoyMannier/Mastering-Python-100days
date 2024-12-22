from turtle import Turtle
MOVE_DISTANCE = 10
FINISH_LINE = 280
START_POSITION = (0, -280)
class TurtleModel(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.start()


    def start(self):
        self.penup()
        self.goto(START_POSITION)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)