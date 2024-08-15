from turtle import Screen, Turtle
import player_one
import time
import pong
import player_two
import scoreboard
import random


def middle_line():
    """create a broken line in the middle."""
    turtle.hideturtle()
    turtle.color("white")
    turtle.teleport(x=0, y=300)

    while turtle.ycor() != -300:
        turtle.setheading(270)
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


# CODE HERE ----------------------------------------------------
turtle = Turtle()
screen = Screen()

screen_x = 800
screen_y = 600
screen.bgcolor("black")
screen.setup(width=screen_x, height=screen_y)
screen.listen()
screen.tracer(0)

# TODO create middle broken line.
middle_line()

# TODO create and move a paddle.
player1 = player_one.Paddle()
player2 = player_two.Paddle2()
score = scoreboard.Scoreboard()

# TODO create a Pong ball.
pong = pong.Pong()

# TODO key bindings.
screen.onkeyrelease(key="W", fun=player1.up)
screen.onkeyrelease(key="w", fun=player1.up)
screen.onkeyrelease(key="S", fun=player1.down)
screen.onkeyrelease(key="s", fun=player1.down)
screen.onkeyrelease(key="Up", fun=player2.up)
screen.onkeyrelease(key="Down", fun=player2.down)


def start_game():

    # TODO set Pong random heading.
    pong.refresh()

    is_game_on = True
    while is_game_on:
        pong.move_pong()
        screen.update()
        time.sleep(0.05)

        # TODO detect collision with wall and bounce.
        if pong.ycor() > 280 or pong.ycor() < -280:
            pong.wall_hit_change_heading()

        # TODO detect collision with paddle.
        # used loop comprehension.
        [(pong.p1_hit_change_heading()) for paddle in player1.segment_list if paddle.distance(pong) < 15]
        [(pong.p2_hit_change_heading()) for paddle in player2.segment_list if paddle.distance(pong) < 15]

        # TODO detect when paddle missed the pong and hit the left or right edge.
        if pong.xcor() > 390:
            is_game_on = False
            score.player1_score += 1

        elif pong.xcor() < -390:
            is_game_on = False
            score.player2_score += 1

    pong.refresh()
    score.update_score()


# -------------------------------------------------------------------------------

is_game_over = False
while not is_game_over:
    start_game()

    if score.player1_score >= 10 or score.player2_score >= 10:
        is_game_over = True
        score.game_over()

screen.exitonclick()
