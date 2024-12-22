from turtle import Turtle
from random import choice, randint
import time

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
STARTING_MOVE_DISTANCE = 5
MOVE_INCR = 10
class CarManager:
    def __init__(self):
        self.cars = []

    def generate_cars(self):
        car = Turtle(shape="square")
        car.color(choice(colors))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(300, randint(-250, 250))

        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        STARTING_MOVE_DISTANCE += MOVE_INCR
