
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=600)
screen.bgpic("screen.png")
screen.title("PONG")
user_choice = screen.textinput(title="user choice", prompt="choose your paddle (right or left) : ").lower()
screen.tracer(0)
user_paddle = Paddle(user_choice)
score = Scoreboard()
if user_choice == "right":
    user_choice = "left"
else:
    user_choice = "right"
computer_paddle = Paddle(user_choice)
ball = Ball()
game_is_on = True
screen.listen()
screen.onkey(fun=user_paddle.up, key="Up")
screen.onkey(fun=user_paddle.down, key="Down")
screen.tracer(0)

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect the collision of ceiling and floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(user_paddle.paddle) < 50 and ball.xcor() > 400 or ball.distance(computer_paddle.paddle) < 50 and \
            ball.xcor() < -400:
        ball.bounce_x()
    # Detect the scores

    if ball.xcor() > 450:
        ball.rest_position()
        if user_choice == "right":
            score.add_user_score()
        else:
            score.add_computer_score()

    if ball.xcor() < -450:
        ball.rest_position()
        if user_choice == "right":
            score.add_computer_score()
        else:
            score.add_user_score()

screen.exitonclick()


