from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
from scoreboard import Scoreboard

# TODO create screen with 800 x 600.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # turn off animation. !must have screen update method after!

# TODO create a left and right paddle. what is the inconsistent value of the paddle?
#  answer: x and y position. make it as a parameter.
left_paddle = Paddle(-380, 0)
right_paddle = Paddle(370, 0)

# TODO create a Pong ball and make it move.
pong = Pong()

# TODO create scoreboard.
score = Scoreboard()

# TODO move the paddles.
screen.listen()  # allow to bind function into keys.
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=left_paddle.move_up, key="W")
screen.onkey(fun=left_paddle.move_down, key="S")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(pong.time_speed)
    pong.move()

    # TODO detect collision with wall and bounce.
    if pong.ycor() >= 290 or pong.ycor() <= -280:
        pong.y_bounce()

    # TODO detect collision with paddle and bounce.
    if (pong.xcor() == -360 and pong.distance(left_paddle) < 60 or pong.xcor() == 350 and pong.distance(right_paddle) <
            60):
        pong.x_bounce()

    # TODO detect if paddles missed the pong.
    if pong.xcor() > 370:
        score.right_add_point()
        pong.reset_pos()

    if pong.xcor() < -380:
        score.left_add_point()
        pong.reset_pos()

    score.update_score()

screen.exitonclick()
