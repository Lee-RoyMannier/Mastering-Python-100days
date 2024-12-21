from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreL = 0
        self.scoreR = 0

        self.hideturtle()
        self.penup()
        self.goto(0,240)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'{self.scoreL} {self.scoreR}', align='center', font=('Arial', 36))
