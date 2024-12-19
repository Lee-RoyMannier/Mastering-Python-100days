from turtle import Screen, Turtle
from turtle_model import TurtleModel
from random import choice, randint

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput("use choice", "pls enter the color winner")

colors = ["red", "orange", "yellow", "green", "blue", "black"]
POS = [(-230, -70), (-230, -40), (-230, -10), (-230, 20), (-230, 50), (-230, 80)]
turtles = [TurtleModel(POS[position][0], POS[position][1], colors[position]) for position in range(0, len(POS))]

race = True
while race:
    for t in turtles:
        t.run()
        if t.xcor() >= 230:
            print(f"Turtle {t.pencolor()} wins!")
            if user_choice == t.pencolor():
                print("Nice one ! ")
            else:
                print("Nope ! You loose")
            race = False

screen.exitonclick()