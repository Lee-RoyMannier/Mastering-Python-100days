from turtle import Turtle
import json

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        try:
            file = open("score.json", "r")
            self.best_score = int(json.load(file))
            file.close()
        except FileNotFoundError:
            file = open("score.json", "w")
            self.best_score = 0
            file.write(str(self.best_score))

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, best score {self.best_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        if self.score >= self.best_score:
            self.best_score = self.score
            self.update_file()
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))


    def update_file(self):
        file = open("score.json", "w")
        file.write(json.dumps(self.best_score, indent=4))
        file.close()