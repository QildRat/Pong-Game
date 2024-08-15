from turtle import Turtle
from player_one import Paddle

PADDLE_POS = [40, 20, 0, -20, -40]
RIGHT_PADDLE_POS = 380


class Paddle2(Paddle):

    def __init__(self):
        super().__init__()

    def create_paddle(self):
        for position in PADDLE_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.teleport(x=RIGHT_PADDLE_POS, y=position)
            self.segment_list.append(new_segment)
