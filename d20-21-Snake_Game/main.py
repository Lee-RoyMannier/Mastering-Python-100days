from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.update_position()

    if snake.head.distance(food) <= 15:
        scoreboard.increase_score()
        snake.add_segment()
        food.generate_food()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            game = False

    if snake.head.xcor() > 300 or snake.head.xcor() < -300:
        y_cor = snake.head.ycor()
        x_cor = snake.head.xcor() * (-1)
        snake.head.goto(x=x_cor, y=y_cor)

    elif snake.head.ycor() > 300 or snake.head.ycor() < -300:
        x_cor = snake.head.xcor()
        y_cor = snake.head.ycor() * (-1)
        snake.head.goto(x=x_cor, y=y_cor)

screen.exitonclick()