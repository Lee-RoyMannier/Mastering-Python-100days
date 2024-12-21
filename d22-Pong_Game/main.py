import time
from turtle import Screen
from pad import Pad
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
screen.bgcolor('black')
screen.title("Pong Game")

left_paddle = Pad(x_cord=-380, y_cord=50)
right_paddle = Pad(x_cord=380, y_cord=50)
ball = Ball()

screen.onkey(left_paddle.move_up, 'Up')
screen.onkey(left_paddle.move_down, 'Down')
screen.onkey(right_paddle.move_up, 'w')
screen.onkey(right_paddle.move_down, 's')

while True:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()