from turtle import Screen
from turtle_model import TurtleModel, FINISH_LINE
from cars import CarManager
from scoreboard import Scoreboard
import time
from random import randint
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road")
screen.bgcolor("white")
screen.tracer(0)

turtle_m = TurtleModel()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=turtle_m.move_up)
screen.onkey(key="Down", fun=turtle_m.move_down)


car_manager = CarManager()

while True:
    random_car = randint(1,6)
    screen.update()
    time.sleep(0.1)
    if random_car == 6:
        car_manager.generate_cars()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(turtle_m) < 20:
            scoreboard.restart()
            turtle_m.start()

    if turtle_m.ycor() > FINISH_LINE:
        scoreboard.increase_level()
        car_manager.increase_speed()
        turtle_m.start()

screen.exitonclick()