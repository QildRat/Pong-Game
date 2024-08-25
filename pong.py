from turtle import Turtle

TIME_SPEED = 0.05
SPEED_UP_VALUE = 0.9


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_value = 5
        self.x_value = 5
        self.time_speed = TIME_SPEED

    def move(self):
        """increment the current value of xcor and ycor."""
        new_x = self.xcor() + self.x_value
        new_y = self.ycor() + self.y_value
        self.goto(new_x, new_y)

    def y_bounce(self):
        """return negative or positive value of the y"""
        self.y_value *= -1

    def x_bounce(self):
        """return negative or positive value of the x. speed up pong on every hit of the paddle."""
        self.x_value *= -1
        self.speed_up()

    def reset_pos(self):
        """reset the pong to home position and reset its speed. go to opposite direction where it's missed."""
        self.home()
        self.x_value *= -1
        self.time_speed = TIME_SPEED

    def speed_up(self):
        """return the reduced value of refresh rate."""
        self.time_speed *= SPEED_UP_VALUE
