from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.start_game()


    def start_game(self):
        self.clear()
        self.level = 1
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align='center', font=('Arial', 20, 'bold'))

    def restart(self):
        self.start_game()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=('Arial', 20, 'bold'))
