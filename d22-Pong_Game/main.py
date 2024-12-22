import time
from turtle import Screen
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
screen.bgcolor('black')
screen.title("Pong Game")

left_paddle = Pad(x_cord=-350, y_cord=0)
right_paddle = Pad(x_cord=350, y_cord=0)
ball = Ball()

screen.onkey(left_paddle.move_up, 'Up')
screen.onkey(left_paddle.move_down, 'Down')
screen.onkey(right_paddle.move_up, 'w')
screen.onkey(right_paddle.move_down, 's')

while True:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290 :
        ball.bounce_y()

    if ball.distance(left_paddle) < 40 and ball.xcor() < -320 or ball.distance(right_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        left_paddle.reset_pad(-350,0)
        right_paddle.reset_pad(350, 0)
        ball.restart()
        scoreboard.scoreR += 1
        scoreboard.display_score()

    elif ball.xcor() < -380:
        left_paddle.reset_pad(-350, 0)
        right_paddle.reset_pad(350, 0)
        ball.restart()
        scoreboard.scoreL += 1
        scoreboard.display_score()



screen.exitonclick()