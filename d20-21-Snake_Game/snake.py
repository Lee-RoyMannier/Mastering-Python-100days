from turtle import Turtle

class Snake():
    def __init__(self):
        self.POSITION = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_body()
        self.head = self.segments[0]


    def create_body(self):
        for pos in self.POSITION:
            self.create_segment(pos)

    def create_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def add_segment(self):
        last_segment = self.segments[-1]
        position = last_segment.position()
        self.create_segment(position)
    def update_position(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

