from turtle import Turtle
import random

NORTH_EAST = 45
NORTH_WEST = 135
SOUTH_EAST = 315
SOUTH_WEST = 225
HEADING_LIST = [NORTH_WEST, NORTH_EAST, SOUTH_EAST, SOUTH_WEST]


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")

    def move_pong(self):
        self.forward(20)

    def refresh(self):
        self.penup()
        self.home()
        self.setheading(random.choice(HEADING_LIST))

    def wall_hit_change_heading(self):
        bounce_heading = (self.heading() - 360) * -1    # prevent negative value.
        self.setheading(bounce_heading)

    def p1_hit_change_heading(self):
        if self.heading() == NORTH_WEST:
            self.setheading(NORTH_EAST)
        elif self.heading() == SOUTH_WEST:
            self.setheading(SOUTH_EAST)

    def p2_hit_change_heading(self):
        if self.heading() == SOUTH_EAST:
            self.setheading(SOUTH_WEST)
        elif self.heading() == NORTH_EAST:
            self.setheading(NORTH_WEST)
