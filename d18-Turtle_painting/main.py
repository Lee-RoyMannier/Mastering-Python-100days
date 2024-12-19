from turtle import Turtle, Screen
from random import choice


dot_painting = Turtle()
dot_painting.hideturtle()
dot_painting.speed("fastest")
screen = Screen()

dot_painting.penup()
dot_painting.setheading(225)
dot_painting.forward(300)
dot_painting.setheading(0)
nb_dot = 100
colors_tuple = ["yellow", "red", "green", "blue", "purple", "black", "brown", "pink"]

for i in range(1, nb_dot+1):
    dot_painting.dot(15, choice(colors_tuple))
    dot_painting.forward(50)

    if i % 10 == 0:
        dot_painting.setheading(90)
        dot_painting.forward(50)
        dot_painting.setheading(180)
        dot_painting.forward(500)
        dot_painting.setheading(0)

screen.exitonclick()